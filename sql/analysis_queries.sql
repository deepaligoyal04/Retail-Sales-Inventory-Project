-- Run these queries in SQLite after creating retail_store.db.

-- 1. Overall business summary
SELECT SUM(total_amount) AS total_revenue,
       COUNT(DISTINCT order_id) AS total_orders,
       SUM(quantity) AS units_sold
FROM sales;

-- 2. Monthly revenue
SELECT substr(order_date, 1, 7) AS month,
       SUM(total_amount) AS revenue
FROM sales
GROUP BY month
ORDER BY month;

-- 3. Best-performing products
SELECT product_name,
       SUM(quantity) AS units_sold,
       SUM(total_amount) AS revenue
FROM sales
GROUP BY product_name
ORDER BY revenue DESC;

-- 4. City-wise performance
SELECT city,
       COUNT(DISTINCT order_id) AS orders,
       SUM(total_amount) AS revenue
FROM sales
GROUP BY city
ORDER BY revenue DESC;

-- 5. Products requiring stock replenishment
SELECT product_name, stock_quantity, reorder_level
FROM inventory
WHERE stock_quantity <= reorder_level;
