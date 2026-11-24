from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(17)
products = [
    ("P001", "Notebook", "Stationery", 45, 180),
    ("P002", "Pen Pack", "Stationery", 30, 350),
    ("P003", "Water Bottle", "Accessories", 160, 90),
    ("P004", "Backpack", "Accessories", 650, 55),
    ("P005", "Desk Lamp", "Electronics", 420, 40),
    ("P006", "File Folder", "Stationery", 25, 280),
    ("P007", "Calculator", "Electronics", 350, 65),
    ("P008", "Mouse", "Electronics", 280, 70),
    ("P009", "USB Drive", "Electronics", 390, 50),
    ("P010", "Lunch Box", "Accessories", 220, 75),
    ("P011", "Sticky Notes", "Stationery", 35, 240),
    ("P012", "Headphones", "Electronics", 780, 35),
]

n = 1800
dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 330, n), unit="D")
rows = []
for i in range(n):
    product = products[int(rng.integers(0, len(products)))]
    qty = int(rng.integers(1, 6))
    rows.append({
        "order_id": f"ORD{i + 1:05d}",
        "order_date": dates[i].date().isoformat(),
        "product_id": product[0],
        "product_name": product[1],
        "category": product[2],
        "quantity": qty,
        "unit_price": product[3],
        "total_amount": qty * product[3],
        "city": rng.choice(["Delhi", "Noida", "Ghaziabad", "Gurugram", "Faridabad"]),
        "payment_mode": rng.choice(["UPI", "Card", "Cash"]),
    })

sales = pd.DataFrame(rows)
sales.to_csv(DATA / "sales.csv", index=False)

inventory = pd.DataFrame([
    {
        "product_id": p[0],
        "product_name": p[1],
        "category": p[2],
        "unit_price": p[3],
        "stock_quantity": p[4],
        "reorder_level": 30,
    }
    for p in products
])
inventory.to_csv(DATA / "inventory.csv", index=False)
print(f"Generated {len(sales)} sales rows and {len(inventory)} inventory products.")
