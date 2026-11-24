from pathlib import Path
import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "retail_store.db"

st.set_page_config(
    page_title="Retail Sales & Inventory Manager",
    page_icon="🛒",
    layout="wide",
)

st.title("🛒 Retail Sales & Inventory Management System")
st.caption("A simple dashboard to understand sales performance and monitor product stock.")

if not DB_PATH.exists():
    st.warning("The database has not been created yet.")
    st.code("python scripts/generate_data.py\npython src/setup_database.py")
    st.stop()

@st.cache_data
def load_data():
    with sqlite3.connect(DB_PATH) as con:
        sales = pd.read_sql_query("SELECT * FROM sales", con, parse_dates=["order_date"])
        inventory = pd.read_sql_query("SELECT * FROM inventory", con)
    return sales, inventory

sales, inventory = load_data()
if sales.empty:
    st.error("No sales data found. Regenerate the sample data and database.")
    st.stop()

st.sidebar.header("Dashboard Filters")
city_options = sorted(sales["city"].dropna().unique().tolist())
category_options = sorted(sales["category"].dropna().unique().tolist())
selected_cities = st.sidebar.multiselect("City", city_options, default=city_options)
selected_categories = st.sidebar.multiselect("Category", category_options, default=category_options)

date_min = sales["order_date"].min().date()
date_max = sales["order_date"].max().date()
date_range = st.sidebar.date_input(
    "Order date range",
    value=(date_min, date_max),
    min_value=date_min,
    max_value=date_max,
)

filtered = sales[
    sales["city"].isin(selected_cities)
    & sales["category"].isin(selected_categories)
].copy()
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        filtered["order_date"].dt.date.between(start_date, end_date)
    ]

if filtered.empty:
    st.info("No sales records match these filters. Change the filters to see results.")
    st.stop()

revenue = float(filtered["total_amount"].sum())
order_count = int(filtered["order_id"].nunique())
units_sold = int(filtered["quantity"].sum())
avg_order_value = float(filtered.groupby("order_id")["total_amount"].sum().mean())

low_stock = inventory[inventory["stock_quantity"] <= inventory["reorder_level"]].copy()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Revenue", f"₹{revenue:,.0f}")
k2.metric("Orders", f"{order_count:,}")
k3.metric("Units Sold", f"{units_sold:,}")
k4.metric("Low-stock Products", f"{len(low_stock)}")

sales_tab, inventory_tab, insights_tab = st.tabs([
    "📊 Sales Analysis", "📦 Inventory Management", "💡 Business Insights"
])

with sales_tab:
    st.subheader("Monthly Revenue Trend")
    monthly = (
        filtered.assign(month=filtered["order_date"].dt.to_period("M").astype(str))
        .groupby("month", as_index=False)
        .agg(revenue=("total_amount", "sum"))
    )
    st.plotly_chart(
        px.line(monthly, x="month", y="revenue", markers=True,
                labels={"month": "Month", "revenue": "Revenue (₹)"}),
        use_container_width=True,
    )

    left, right = st.columns(2)
    product_summary = (
        filtered.groupby("product_name", as_index=False)
        .agg(revenue=("total_amount", "sum"), units_sold=("quantity", "sum"))
        .sort_values("revenue", ascending=False)
        .head(10)
    )
    left.plotly_chart(
        px.bar(product_summary.sort_values("revenue"), x="revenue", y="product_name",
               orientation="h", title="Top 10 Products by Revenue",
               labels={"revenue": "Revenue (₹)", "product_name": "Product"}),
        use_container_width=True,
    )

    city_summary = (
        filtered.groupby("city", as_index=False)
        .agg(revenue=("total_amount", "sum"))
        .sort_values("revenue", ascending=False)
    )
    right.plotly_chart(
        px.bar(city_summary, x="city", y="revenue", title="Revenue by City",
               labels={"revenue": "Revenue (₹)", "city": "City"}),
        use_container_width=True,
    )

    st.subheader("Sales Records")
    st.dataframe(
        filtered.sort_values("order_date", ascending=False),
        use_container_width=True,
        hide_index=True,
    )

with inventory_tab:
    st.subheader("Current Inventory")
    inventory_view = inventory.copy()
    inventory_view["status"] = inventory_view.apply(
        lambda row: "Reorder Required"
        if row["stock_quantity"] <= row["reorder_level"]
        else "Stock Available",
        axis=1,
    )
    st.plotly_chart(
        px.bar(
            inventory_view, x="product_name", y="stock_quantity", color="status",
            title="Available Stock by Product",
            labels={"product_name": "Product", "stock_quantity": "Units in Stock"},
        ),
        use_container_width=True,
    )
    st.dataframe(inventory_view, use_container_width=True, hide_index=True)

    st.subheader("Products Requiring Reorder")
    if low_stock.empty:
        st.success("No products are currently below their reorder level.")
    else:
        st.warning(f"{len(low_stock)} product(s) need a stock review.")
        st.dataframe(low_stock, use_container_width=True, hide_index=True)

with insights_tab:
    st.subheader("Business Insights")
    top_product = (
        filtered.groupby("product_name")["total_amount"].sum().idxmax()
    )
    top_city = filtered.groupby("city")["total_amount"].sum().idxmax()
    top_payment = filtered.groupby("payment_mode")["total_amount"].sum().idxmax()

    st.write(f"• **{top_product}** is the highest-revenue product in the selected data.")
    st.write(f"• **{top_city}** is the highest-revenue city in the selected data.")
    st.write(f"• **{top_payment}** is the most-used revenue-generating payment mode in the selected data.")
    st.write(f"• Average order value for the selected data is **₹{avg_order_value:,.2f}**.")
    if not low_stock.empty:
        names = ", ".join(low_stock["product_name"].astype(str).tolist())
        st.write(f"• Review stock replenishment for: **{names}**.")
    else:
        st.write("• All listed products are above their reorder thresholds.")

    payment_summary = (
        filtered.groupby("payment_mode", as_index=False)
        .agg(revenue=("total_amount", "sum"))
    )
    st.plotly_chart(
        px.pie(payment_summary, names="payment_mode", values="revenue",
               title="Revenue by Payment Mode", hole=0.35),
        use_container_width=True,
    )

st.divider()
st.caption("Project demonstration using sample retail data. Replace the CSV files with authorised store data for a real deployment.")
