# Internship Project Report Guide
## Project: Retail Sales & Inventory Management System

Use this as the writing base for the report format supplied in the internship guidelines. Fill in the student details and add screenshots captured from your own run of the project. Report actual values from your dashboard; do not invent results.

# Cover Page
**Retail Sales & Inventory Management System**  
Internship Report – IBM SkillsBuild Big Data & Business Management Internship  
Student Name(s): [Member 1] and [Member 2]  
Roll Number(s): [Roll Numbers]  
Course / Branch: [Course and Branch]  
Semester / Section: [Semester and Section]  
Institute: [Institute Name]  
Academic Year: [Year]

# Inner Pages

## A. Certificate
Insert the official internship completion certificate issued to the student(s). Do not edit or recreate an official certificate.

## B. Student Declaration
We hereby declare that the project titled “Retail Sales & Inventory Management System” is the work completed by us as part of our internship/project learning activity. The sources and references used have been acknowledged in the report.

## C. Acknowledgement
We express our sincere gratitude to the internship organisers, trainers, faculty coordinator and our institute for their guidance and support. We also thank everyone who helped us understand the project requirements and complete the implementation.

# 1. About Company / Industry / Institute
This project is based on the retail industry. Retail stores maintain records of products, quantities sold, prices, dates, payment modes and available stock. Analysing these records helps store managers review business performance and plan stock replenishment. The project demonstrates a small-scale retail business information system using sample transaction data.

# 2. Table of Contents
Add the final page numbers after formatting the report.

# 3. List of Tables
Suggested tables:
- Table 1: Software and hardware requirements
- Table 2: Sales dataset fields
- Table 3: Inventory dataset fields
- Table 4: Dashboard KPI summary

# 4. List of Figures
Suggested figures:
- Figure 1: Project workflow
- Figure 2: Main dashboard
- Figure 3: Monthly revenue chart
- Figure 4: Top products chart
- Figure 5: Inventory stock chart

# 5. Abbreviations and Nomenclature
- KPI – Key Performance Indicator
- DBMS – Database Management System
- SQL – Structured Query Language
- CSV – Comma-Separated Values
- UI – User Interface

# 6. Abstract
The Retail Sales & Inventory Management System is a beginner-friendly business analytics application designed to organise retail sales and inventory information. The system uses Python and Pandas to validate and prepare transaction records, SQLite to store structured data, and Streamlit with Plotly to display the results in an interactive dashboard. The dashboard presents key indicators such as total revenue, order count, units sold and average order value. It also provides monthly revenue trends, product performance, city-wise sales, payment-mode analysis and stock-level alerts. The project demonstrates how basic data management and visualisation can help a retail business review its performance and identify products that may require replenishment.

# 7. Chapters

## Chapter 1 – Introduction
Retail stores generate transaction records every day. These records contain details about products, quantities, prices, dates and payment methods. Inventory records contain information about the quantity of each product currently available. If these records are not reviewed regularly, a store may find it difficult to identify top-selling products or products that need replenishment.

The proposed system brings basic sales and inventory analysis into one dashboard. It is designed as a small demonstration project that can be understood and explained by beginner-level developers.

### Objectives
1. Organise sales and inventory records.
2. Validate and clean the transaction data.
3. Store structured records in a local database.
4. Calculate key sales indicators.
5. Identify top products and high-performing cities.
6. Highlight products at or below their reorder level.
7. Present business information through an interactive dashboard.

## Chapter 2 – Literature Survey (if required)
Business information systems commonly use structured data storage, data processing and visualisation to support routine business decisions. Spreadsheet applications can organise small datasets, while relational databases provide tables and queries for structured records. Dashboards present key measures and trends in a form that is easier to interpret. This project applies these basic concepts using Pandas, SQLite and Streamlit.

Add course materials or articles actually consulted by the team if your faculty requires formal literature references. Do not add references that were not read.

## Chapter 3 – Problem Statement
A small retail store may maintain sales and inventory records but may not have one consolidated view of its business performance. Manual calculations can make it time-consuming to compare monthly revenue, identify top products, review city-wise sales and notice low-stock products. The project addresses this problem by creating a simple database-backed dashboard for sales and inventory analysis.

## Chapter 4 – Description of Various Training Modules
1. **Python fundamentals:** variables, data types, conditions, loops, functions and file handling.
2. **Tabular data processing:** reading CSV files and working with Pandas DataFrames.
3. **Data cleaning:** checking missing values, validating numeric fields and preparing date columns.
4. **Database fundamentals:** tables, records, indexes and SQL queries using SQLite.
5. **Business analytics:** calculating revenue, orders, units sold and average order value.
6. **Data visualisation:** creating charts using Plotly.
7. **Dashboard development:** presenting KPIs, filters, tables and charts using Streamlit.
8. **Project integration:** connecting the cleaned data and database to the dashboard.

## Chapter 5 – Methodology Adopted

### 5.1 Design of Experiment / Flow Chart
The system follows this sequence:

```text
Sales and Inventory CSV Files
              |
              v
      Python and Pandas
              |
              v
     Data Cleaning and Checks
              |
              v
        SQLite Database
              |
              v
   Sales and Inventory Analysis
              |
              v
      Streamlit Dashboard
              |
              v
  Charts, KPIs and Stock Alerts
              |
              v
       Business Insights
```

### 5.2 Machines and Materials / Hardware and Software Used
**Hardware:** Laptop or desktop computer, recommended minimum 4 GB RAM, and internet access for installing the Python packages.

**Software:** Python 3.10 or 3.11, Pandas, SQLite, Streamlit, Plotly, Visual Studio Code or another Python editor, and a web browser.

**Input files:** `sales.csv` and `inventory.csv`, supplied as sample project data.

### 5.3 Optimisation / Data Flow Diagram and Algorithms Used
**Data flow:** CSV input → Pandas validation and cleaning → SQLite tables → SQL/Pandas aggregation → Streamlit dashboard.

**Algorithms and business logic:**
- **Data validation:** remove rows with missing essential fields and invalid quantity or price values.
- **Revenue calculation:** `Total Amount = Quantity × Unit Price`.
- **Monthly aggregation:** group sales by year and month and calculate total revenue.
- **Product aggregation:** group transactions by product and calculate revenue and units sold.
- **City aggregation:** group transactions by city and calculate revenue.
- **Reorder rule:** if `Stock Quantity <= Reorder Level`, mark the product as “Reorder Required”.
- **Top product identification:** select the product with the highest total revenue in the filtered records.

**Basic optimisation:** the application stores prepared records in SQLite and uses grouped summaries for charts rather than manually calculating each displayed value.

### 5.4 Characterisations / Snapshots of Results Obtained
Insert screenshots captured from your running application:
- Figure 1: Main dashboard and KPI cards.
- Figure 2: Monthly revenue trend.
- Figure 3: Top 10 products by revenue.
- Figure 4: Inventory levels and reorder status.
- Figure 5: City-wise revenue and payment-mode analysis.

Write one or two sentences below each figure explaining what the screenshot demonstrates.

## Chapter 6 – Results and Discussions
After running the dashboard, enter the actual values shown:
- Total revenue: [value from dashboard]
- Total orders: [value from dashboard]
- Units sold: [value from dashboard]
- Number of low-stock products: [value from dashboard]
- Highest revenue product: [value from dashboard]
- Highest revenue city: [value from dashboard]

Discuss the monthly revenue pattern, products contributing the most revenue, cities with higher sales and products requiring stock review. The included dataset is generated sample data, so clearly identify it as sample data in the report.

## Chapter 7 – Conclusions
The project demonstrates a simple retail sales and inventory analysis workflow. It combines data validation, local database storage, business calculations and dashboard visualisation. The dashboard helps users review sales performance, compare products and cities, and identify stock that may require replenishment. The implementation provides practical experience with Python, Pandas, SQLite, Streamlit and Plotly.

### Future Scope
The system may later be extended with login functionality, sales-entry forms, supplier details, automatic stock updates after a sale and report export.

## Chapter 8 – References / Bibliography
List only resources actually used. Official documentation:
- Python: https://docs.python.org/3/
- Pandas: https://pandas.pydata.org/docs/
- SQLite: https://www.sqlite.org/docs.html
- Streamlit: https://docs.streamlit.io/
- Plotly: https://plotly.com/python/

# Suggested Equal Work Distribution for Two Members

**Member 1 – Data and Database (50%)**
- Prepare and validate sales/inventory CSV data.
- Implement Pandas cleaning and calculations.
- Create SQLite tables and indexes.
- Write and test SQL queries.
- Prepare report sections: Introduction, Problem Statement, Literature Survey, Data Processing and Database Design.

**Member 2 – Dashboard and Business Analysis (50%)**
- Build the Streamlit dashboard layout and filters.
- Create Plotly charts and KPI cards.
- Implement inventory status and reorder alerts.
- Prepare business insights and dashboard testing.
- Prepare report sections: Training Modules, Dashboard Design, Results and Discussions, Business Recommendations.

**Both members**
- Integrate and test the complete application.
- Capture screenshots, verify results, write conclusion and prepare the presentation.
- Both should understand the complete workflow for viva.
