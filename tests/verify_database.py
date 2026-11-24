from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "retail_store.db"

with sqlite3.connect(DB) as con:
    sales_count = con.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
    product_count = con.execute("SELECT COUNT(*) FROM inventory").fetchone()[0]
    invalid_sales = con.execute(
        "SELECT COUNT(*) FROM sales WHERE quantity <= 0 OR unit_price < 0"
    ).fetchone()[0]

assert sales_count > 0, "Sales table is empty"
assert product_count > 0, "Inventory table is empty"
assert invalid_sales == 0, "Invalid sales rows found"
print(f"Database verification passed: {sales_count} sales rows, {product_count} products.")
