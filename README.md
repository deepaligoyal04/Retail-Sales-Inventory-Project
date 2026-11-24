# Retail Sales & Inventory Management System

## Project overview
This project is a small retail-store management and business analytics system. It uses sales and inventory records to show how much the store sells, which products perform well, and which items may need replenishment.

The project is intentionally beginner-friendly and uses a small, understandable technology stack.

## Technology used
- **Python** – main programming language
- **Pandas** – data cleaning and calculations
- **SQLite** – local database for sales and inventory
- **Streamlit** – dashboard interface
- **Plotly** – interactive charts

No PySpark, PyTorch, machine learning, cloud deployment, or Java is required.

## Main features
1. Load sales and inventory CSV files.
2. Validate and clean sales records.
3. Store the cleaned records in SQLite.
4. Calculate revenue, orders, units sold and average order value.
5. Show monthly sales and top products.
6. Compare sales across cities and payment methods.
7. Show available stock and flag products at or below their reorder level.
8. Display simple business insights.

## Project structure
```text
Retail_Sales_Inventory_Project/
├── app.py
├── requirements.txt
├── retail_store.db
├── data/
│   ├── sales.csv
│   └── inventory.csv
├── scripts/
│   └── generate_data.py
├── src/
│   └── setup_database.py
├── sql/
│   └── analysis_queries.sql
└── report/
    └── REPORT_GUIDE.md
```

## Installation and execution
Python 3.10 or 3.11 is recommended.

### 1. Create and activate a virtual environment
```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate sample data (optional)
The ZIP already includes sample CSV files. Run this command only if you want to regenerate them:
```bash
python scripts/generate_data.py
```

### 4. Create or refresh the database
```bash
python src/setup_database.py
```

### 5. Launch the dashboard
```bash
streamlit run app.py
```

## Dashboard sections
- Sales Analysis
- Inventory Management
- Business Insights

## Business rule
A product is marked **Reorder Required** when its current stock quantity is less than or equal to its configured reorder level. This is a simple threshold rule, not a demand forecasting model.

## Data note
The included CSVs are sample/demo data generated for this project. Do not present the sample figures as actual company sales.
