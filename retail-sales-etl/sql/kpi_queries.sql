# KPI-1 Total Revenue

SELECT
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM fact_sales;

# KPI-2 Revenue by Day

SELECT
    date_id,
    ROUND(SUM(total_amount), 2) AS revenue
FROM fact_sales
GROUP BY date_id
ORDER BY date_id

# KPI-3 Total 10 Products

SELECT
    product_id,
    ROUND(SUM(total_amount), 2) AS revenue
FROM fact_sales
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;

# KPI-4 Revenue by Region

SELECT 
    ds.region,
    ROUND(SUM(fs.total_amount), 2) AS revenue
FROM fact_sales fs
JOIN dim_store ds
ON fs.store_id = ds.store_id
GROUP BY ds.region
ORDER BY revenue DESC;

# KPI-5 Payment Method Distribution

SELECT
    payment_method,
    COUNT(*) AS transactions,
    ROUND(SUM(total_amount), 2) AS revenue
FROM fact_sales
GROUP BY payment_method
ORDER BY revenue DESC;


