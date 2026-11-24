from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DB_PATH = ROOT / "retail_store.db"

def prepare_data():
    sales_path = DATA_DIR / "sales.csv"
    inventory_path = DATA_DIR / "inventory.csv"
    if not sales_path.exists() or not inventory_path.exists():
        raise FileNotFoundError("CSV files missing. Run: python scripts/generate_data.py")

    sales = pd.read_csv(sales_path)
    inventory = pd.read_csv(inventory_path)

    required_sales = {
        "order_id", "order_date", "product_id", "product_name", "category",
        "quantity", "unit_price", "total_amount", "city", "payment_mode"
    }
    missing = required_sales.difference(sales.columns)
    if missing:
        raise ValueError(f"Sales data is missing columns: {sorted(missing)}")

    sales["order_date"] = pd.to_datetime(sales["order_date"], errors="coerce")
    for col in ["quantity", "unit_price", "total_amount"]:
        sales[col] = pd.to_numeric(sales[col], errors="coerce")

    sales = sales.dropna(subset=[
        "order_id", "order_date", "product_id", "quantity", "unit_price"
    ]).copy()
    sales = sales[(sales["quantity"] > 0) & (sales["unit_price"] >= 0)].copy()
    # Recalculate amount to avoid inconsistent source values.
    sales["total_amount"] = sales["quantity"] * sales["unit_price"]
    sales["order_date"] = sales["order_date"].dt.strftime("%Y-%m-%d")

    inventory_required = {
        "product_id", "product_name", "category", "unit_price",
        "stock_quantity", "reorder_level"
    }
    missing_inventory = inventory_required.difference(inventory.columns)
    if missing_inventory:
        raise ValueError(f"Inventory data is missing columns: {sorted(missing_inventory)}")

    for col in ["unit_price", "stock_quantity", "reorder_level"]:
        inventory[col] = pd.to_numeric(inventory[col], errors="coerce")
    inventory = inventory.dropna(subset=[
        "product_id", "product_name", "unit_price", "stock_quantity", "reorder_level"
    ]).copy()
    inventory = inventory[(inventory["stock_quantity"] >= 0) & (inventory["reorder_level"] >= 0)]

    return sales, inventory

def build_database():
    sales, inventory = prepare_data()
    with sqlite3.connect(DB_PATH) as connection:
        sales.to_sql("sales", connection, if_exists="replace", index=False)
        inventory.to_sql("inventory", connection, if_exists="replace", index=False)

        connection.executescript("""
        CREATE INDEX IF NOT EXISTS idx_sales_date ON sales(order_date);
        CREATE INDEX IF NOT EXISTS idx_sales_product ON sales(product_id);

        DROP VIEW IF EXISTS monthly_sales;
        CREATE VIEW monthly_sales AS
        SELECT substr(order_date, 1, 7) AS month,
               SUM(total_amount) AS revenue,
               COUNT(DISTINCT order_id) AS total_orders,
               SUM(quantity) AS units_sold
        FROM sales
        GROUP BY substr(order_date, 1, 7);

        DROP VIEW IF EXISTS product_performance;
        CREATE VIEW product_performance AS
        SELECT product_id, product_name, category,
               SUM(quantity) AS units_sold,
               SUM(total_amount) AS revenue
        FROM sales
        GROUP BY product_id, product_name, category;
        """)
    print(f"Database ready: {DB_PATH}")
    print(f"Loaded {len(sales):,} sales rows and {len(inventory):,} inventory rows.")

if __name__ == "__main__":
    build_database()
