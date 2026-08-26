pip install pandas openpyxl

import pandas as pd
import random
import numpy as np
import os
from datetime import datetime, timedelta

# Set random seeds for reproducibility
random.seed(42)
np.random.seed(42)

# Create a directory to hold your messy data
output_dir = "Messy_Manufacturing_Data"
os.makedirs(output_dir, exist_ok=True)

# 1. Define Master Data (Products)
products_data = [
    {"ProductID": "PRD-101", "ProductName": "Titanium Widget", "MaterialRequired": "Titanium Alloy", "StandardBuildTime": 2.5},
    {"ProductID": "PRD-102", "ProductName": "Steel Bracket", "MaterialRequired": "Carbon Steel", "StandardBuildTime": 1.0},
    {"ProductID": "PRD-103", "ProductName": "Aluminum Casing", "MaterialRequired": "Raw Aluminum", "StandardBuildTime": 1.5},
    {"ProductID": "PRD-104", "ProductName": "Copper Coil", "MaterialRequired": "Copper Wire", "StandardBuildTime": 0.5},
    {"ProductID": "PRD-105", "ProductName": "Nylon Gear", "MaterialRequired": "Nylon Polymer", "StandardBuildTime": 0.75},
    {"ProductID": "PRD-106", "ProductName": "Rubber Seal", "MaterialRequired": "Synthetic Rubber", "StandardBuildTime": 0.25},
    {"ProductID": "PRD-107", "ProductName": "Glass Panel", "MaterialRequired": "Tempered Glass", "StandardBuildTime": 0.5},
    {"ProductID": "PRD-108", "ProductName": "Motor Unit", "MaterialRequired": "Mixed Components", "StandardBuildTime": 4.0},
    {"ProductID": "PRD-109", "ProductName": "Plastic Housing", "MaterialRequired": "ABS Plastic", "StandardBuildTime": 0.75},
    {"ProductID": "PRD-110", "ProductName": "LED Assembly", "MaterialRequired": "Electronic Components", "StandardBuildTime": 1.25}
]
df_products = pd.DataFrame(products_data)
df_products.to_excel(f"{output_dir}/Master_Products.xlsx", index=False)

# 2. Define Master Data (Machines)
machines_data = [
    {"MachineID": "MACH-A1", "MachineType": "CNC Lathe", "DailyCapacityHours": 16, "Status": "Active"},
    {"MachineID": "MACH-A2", "MachineType": "CNC Lathe", "DailyCapacityHours": 16, "Status": "Active"},
    {"MachineID": "MACH-B1", "MachineType": "Stamping Press", "DailyCapacityHours": 24, "Status": "Active"},
    {"MachineID": "MACH-B2", "MachineType": "Stamping Press", "DailyCapacityHours": 24, "Status": "Maintenance"},
    {"MachineID": "MACH-C1", "MachineType": "Laser Cutter", "DailyCapacityHours": 12, "Status": "Active"},
    {"MachineID": "MACH-D1", "MachineType": "Paint Booth", "DailyCapacityHours": 16, "Status": "Active"},
    {"MachineID": "MACH-D2", "MachineType": "Paint Booth", "DailyCapacityHours": 16, "Status": "Offline"},
    {"MachineID": "MACH-E1", "MachineType": "Assembly Station", "DailyCapacityHours": 24, "Status": "Active"},
    {"MachineID": "MACH-E2", "MachineType": "Assembly Station", "DailyCapacityHours": 24, "Status": "Active"},
    {"MachineID": "MACH-F1", "MachineType": "Quality Testing", "DailyCapacityHours": 12, "Status": "Maintenance"}
]
df_machines = pd.DataFrame(machines_data)
df_machines.to_excel(f"{output_dir}/Master_Machines.xlsx", index=False)

# 3. Generate Orders Data (MESSY)
num_orders = 5000
orders_data = []
start_date = datetime(2026, 8, 1)

for i in range(1, num_orders + 1):
    order_id = f"ORD-{1000 + i}"
    product_id = random.choice(products_data)["ProductID"]
    
    # MESSINESS 1: Inconsistent text casing (15% chance to be lowercase)
    if random.random() < 0.15:
        product_id = product_id.lower()
        
    quantity = random.choice([50, 75, 100, 150, 200, 500, 1000])
    
    # MESSINESS 2: Missing quantities (5% chance to be null)
    if random.random() < 0.05:
        quantity = np.nan
        
    days_to_add = random.randint(5, 150)
    due_date_obj = start_date + timedelta(days=days_to_add)
    
    # MESSINESS 3: Mixed Date Formats
    format_choice = random.choice(["%Y-%m-%d", "%m/%d/%Y", "%d-%b-%Y"])
    due_date_str = due_date_obj.strftime(format_choice)
    
    orders_data.append({
        "OrderID": order_id,
        "ProductID": product_id,
        "Quantity": quantity,
        "DueDate": due_date_str,
        "OrderMonth": due_date_obj.strftime("%Y-%m") # Used to split files
    })

df_orders = pd.DataFrame(orders_data)

# MESSINESS 4: Split Orders into separate EXCEL files by month
orders_folder = f"{output_dir}/Orders_Data"
os.makedirs(orders_folder, exist_ok=True)

for month, group in df_orders.groupby("OrderMonth"):
    # Drop the helper column before saving
    group = group.drop(columns=["OrderMonth"])
    group.to_excel(f"{orders_folder}/Orders_{month}.xlsx", index=False)


# 4. Generate Production Schedule Data (MESSY)
schedule_data = []
active_machines = [m["MachineID"] for m in machines_data if m["Status"] == "Active"]

for index, row in df_orders.iterrows():
    schedule_id = f"SCH-{str(index + 1).zfill(4)}"
    machine_id = random.choice(active_machines)
    
    # MESSINESS 5: Leading/Trailing spaces on Machine IDs (10% chance)
    if random.random() < 0.10:
        machine_id = f"  {machine_id} "
    
    # Extract date for schedule math (handling the messy mixed formats)
    try:
        due_date_obj = pd.to_datetime(row["DueDate"])
    except:
        due_date_obj = start_date # Fallback if parsing fails heavily
        
    days_before_due = random.randint(1, 10)
    start_time = due_date_obj - timedelta(days=days_before_due)
    start_time = start_time.replace(hour=random.randint(6, 16), minute=0)
    
    hours_to_build = random.randint(2, 48)
    end_time = start_time + timedelta(hours=hours_to_build)
    
    # MESSINESS 6: Missing End Times (simulating jobs currently in progress)
    end_time_str = end_time.strftime("%Y-%m-%d %H:%M")
    if random.random() < 0.08:
        end_time_str = np.nan
        
    schedule_data.append({
        "ScheduleID": schedule_id,
        "OrderID": row["OrderID"],
        "MachineID": machine_id,
        "StartTime": start_time.strftime("%Y-%m-%d %H:%M"),
        "EndTime": end_time_str
    })

df_schedule = pd.DataFrame(schedule_data)
# Exported as Excel instead of CSV
df_schedule.to_excel(f"{output_dir}/Production_Schedule.xlsx", index=False)

print(f"Messy Data generation complete! Check the '{output_dir}' folder. All files are now .xlsx!")


