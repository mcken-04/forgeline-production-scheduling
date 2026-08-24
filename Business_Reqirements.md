

# Business Requirements Document (BRD)
**Company:** Forgeline Industries

**Project:** Production Scheduling & Delay Analysis

## 1. Executive Summary
Forgeline Industries requires a robust **Production Scheduling & Delay Analysis** dashboard to serve as a command center for factory operations. The primary objective of this project is to identify physical manufacturing bottlenecks and track machine utilization across the product floor.

## 2. Business Objectives
Currently, the manufacturing floor lacks real time visibility into capacity and production statuses due to several data hurdles:
* **Data Fragmentation:** Operational data is scattered across monthly batch files and contains significant inconsistencies.
* **Data Quality Issues:** The raw data includes mixed date formats, inconsistent text casing, and missing quantities requiring data imputation.
* **Unidentified Bottlenecks:** Floor managers are unable to see when specific equipment is overbooked, leading to cascading scheduling delays.

## 3. Stakeholder & Requirements
| **Stakeholders** | **Key Metric of Interest** | **Desired Outcome** |
| :--- | :--- | :--- |
| **Floor Manager** | Machine Utilization (%) | Identify if machines are sitting idle or critically overworked. |
| **Operations Director** | Bottleneck Analysis | Pinpoint which machine types cause the highest frequency of delayed jobs. |
| **Supply Chain Team** | Material Workload (Hours) | Translate raw order quantities into production hours to aid purchasing. |

## 4. Scope of Work
**In-Scope:**
  * Ingestion and transformation of 5,00 synthetic, intentionally messy order records.
  * Automated ETL pipeline utilizing a "drop and refresh" folder connection.
  * Data modeling via a Star Schema Deployment with a dynamic `CALENDERAUTO` table.
  * Development of a Power BI dashboard featuring KPI scorecards and a Matrix Heatmap.
**Out-of-Scope:**
  * Real time data streaming (the pipeline is batch oriented and updates when ew files are added in the folder.

## 5. Functional Requirements
* **Data Standardization:** Parse mixed data formats (e.g. 2026-08-20 vs. 20-Aug-2026) and unify inconsistent text casing.
* **Null Handling & Cleaning:** Impute missing order quantities with a default batch size of 50, and trim hidden whitespaces from Machine IDs.
* **Metric Calculation:** use advanced DAX measures, incorporating `VAR` and `MAX`, to gracefully handle duplicate records and categorize orders as 'On Time', 'Delayed/ or 'In Progress'.
* **Dashboard Interactivity:** Global slicers for `Date`, `Machine ID`, and `Product Name` alongside a Machine Production Scheduling Heatmap.

## 6. Non-Functional Requirements
* **Usability & UI/UX:** The dashboard layout must follow a clean, high-contrast "Card" design over a light gray background.
* **Semantic Coloring:** The visual hierarchy must strictly enforce the Forgeline Industries brand palette: Forgeline Navy (#1E3A5F) for primary data, Steel Gray (#4B5563) for secondary categories, and Forge Orange (#E85D04) exclusively as an alert color for delayed bottlenecks.
