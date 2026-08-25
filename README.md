# Forgeline Industries: Production Scheduling & Delay Analysis

## Executive Summary
Forgeline Industries currently lacks real time visibility into the root causes of operational bottlenecks across its manufacturing floor. This project implements an automated, end-to-end pipeline and business intelligence dashboard to identify physical manufacturing delays and track machine utilization. By transitioning from scattered monthly batch files to a centralized command center, operations managers can now proactively monitor capacity limits, prevent scheduling cascades, and maintain customer delivery timelines.

## Methodology & Tech Stacks
* **Data Generation (Python):** Simulated 5,000 synthetic , intentionally messy manufacturing orders using the `pandas` library, utilizing a locked random seed (42) to ensure strict reproducibility.
* **Automated ETL Pipeline (Excel / Power Query):** Established a "dropo and refresh" folder connection to automatically append monthly CSV/Excel batch files. Engineered tranformation steps to standardize mixed date formats, unify text casing, trim hidden whitespaces from Machine IDs, and impute missing quantities.
* **Data Modeling (Power BI):** Constructed a Star Schema featuring a dynamic `CALENDERAUTO()` Date table to properly handle time intelligence filtering.
* **Advacned DAX Logic:** Deployed robust measures using variables `(VAR)`, `MAX`, and `LOOKUPVALUE` to bypass inactive relationships and handle dupicate Order IDs without breaking the visualizations.

## Key Metrics Tracked
| **Matric** | **Business Value** |
| :--- | :--- |
| **Machine Utilization %** | Identified whether machines are sitting idle or are critically overworked by dividing Scheduled Hours by Active Daily Capacity. |
| **Production Status** | Dynamically classifies every order 'On Time', 'Delayed', 'In Progress' |
| **Material Workload (Hours)** | Translates raw order quantities into actual production hours required per material to aid supply chain purchasing. |
| **Total Delayed Jobs** | Provides an aggregate count of missed deadline across the manufacturing floor. |

## Executive Dashboard

* **Forgeline Navy (#1E3A5F):** Used for primary, positive data points.
* **Steel Gray (#4B5563):** Used for secondary categories and neutral labels.
* **Forge Orange (#E85D04):** Reserved exclusively as an "alert" color to draw attention to delayed jobs and bottlenecks.

## Dashboard Features and Key Business Insights
* **Machine Scheduling Heatmap (Matrix):** Visally exposed overebooked equipment by using conditional formatting to highlight days where scheduled hours exceed physical machine capacity.
* **Bottleneck Analysis (Clusted Bar Chart):** Breaks down Total Delayed Jobs by specific Machine Types, instantly showing if spcific equipment (e.g. CNC Lathes) iscuasing cascading delays.
* **Resource Demand (Treemap):** Highlights the Material Workload Hours, demonstratiing which raw materials are consumuing the majority of total machine time.
* **Interactive Global Slicers:** Allows floor managers to slice the data instantly by Date, Machine type, or Product Name.

## Strategic Reccomendations
* **Optimize Machine Load:** Re-assign upcoming jobs from heavily overbooked machines (highlighted in the matrix Heatmap) to machines currently sitting idle.
* **Proactive Overtime:** Authorize targeted weekend overtime shifts for specific machine operators when scheduled hours vastly exceed the active daily capacity to prevent missed customer deadlines.
* **Customer Communication:** Contact customers regarding orders flagged in the 'Delayed' status before the missed deadline occurs.

## Repository Structure


# Future Enhancements
* ** Live ERP Integration:** Integrate a live REST API with Python to replace the synthetic manufacturing order genration.
* **Predictive Maintenance Forecast:** Implement a predictive Machine Lerning model with Pythion to forcast the probability of machine downtime based on Scheduled Hours and Active Daily Capacity.
* **Operator Shift Drilldown:** Further analyze machine operator shifts to observe correlations to delayed production statuses.
* **Material Supply Chain Exploration:** Study vendor lead times and material costs for key compenents like Titanium Alloy and Corbon Steel to determine optimal purchasing schedules.
