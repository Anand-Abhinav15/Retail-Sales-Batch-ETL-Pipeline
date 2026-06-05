-- Dimension Tables

CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS dim_product (
    product_id INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS dim_store (
    store_id INT PRIMARY KEY,
    region VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

-- Fact Table

CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id SERIAL PRIMARY KEY,

    customer_id INT,
    product_id INT,
    store_id INT,
    date_id DATE,

    quantity INT,
    unit_price NUMERIC(10,2),
    total_amount NUMERIC(12,2),

    load_timestamp TIMESTAMP,

    FOREIGN KEY (customer_id)
        REFERENCES dim_customer(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES dim_product(product_id),

    FOREIGN KEY (store_id)
        REFERENCES dim_store(store_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

-- Incremental Load Tracking

CREATE TABLE IF NOT EXISTS processed_files (
    file_name VARCHAR(255) PRIMARY KEY,
    processed_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);