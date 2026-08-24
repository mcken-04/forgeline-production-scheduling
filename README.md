# Forgeline Industries: Production Scheduling & Delay Analysis

## Executive Summary
Forgeline Industries currently lacks real time visibility into the root causes of operational bottlenecks across its manufacturing floor. This project implements an automated, end-to-end pipeline and business intelligence dashboard to identify physical manufacturing delays and track machine utilization. By transitioning from scattered monthly batch files to a centralized command center, operations managers can now proactively monitor capacity limits, prevent scheduling cascades, and maintain customer delivery timelines.

## Methodology & Tech Stacks
* **Data Generation (Python):** Simulated 5,000 synthetic , intentionally messy manufacturing orders using the `pandas` library, utilizing a locked random seed (42) to ensure strict reproductibility.
* **Automated ETL Pipeline (Excel / Power Query):** Established a "dropo and refresh" folder connection to automatically append monthly CSV/Excel batch files. Engineered tranformation steps to standardize mixed date formats, unify text casing, trim hidden whitespaces from Machine IDs, and impute missing quantities.
* **Data Modeling (Power BI):** Constructed a Star Schema featuring a dynamic `CALENDERAUTO()` Date table to properly handle time intelligence filtering.
* **Advacned DAX Logic:** Deployed robust measures using variables `(VAR)`, `MAX`, and `LOOKUPVALUE` to bypass inactive relationships and handle dupicate Order IDs without breaking the visualizations.

## Key Metrics Tracked
| **Matric** | **Business Value** |
| :--- | :--- |
| **Machine Utilization %** | Identified whether machines are sitting idle or are critically overworked by dividing Scheduled Hours by Active Daily Capacity. |
| **Production Status** | Dynamically 
