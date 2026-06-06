-- =====================================================
-- DIMENSION TABLES
-- =====================================================

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
    day INT,
    quarter INT
);

-- =====================================================
-- FACT TABLE
-- =====================================================

CREATE TABLE IF NOT EXISTS fact_sales (

    sale_id SERIAL PRIMARY KEY,

    order_id VARCHAR(50) UNIQUE,

    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    store_id INT NOT NULL,
    date_id DATE NOT NULL,

    payment_method VARCHAR(50),

    quantity INT,
    unit_price NUMERIC(10,2),
    total_amount NUMERIC(12,2),

    load_timestamp TIMESTAMP,

    CONSTRAINT fk_customer
        FOREIGN KEY(customer_id)
        REFERENCES dim_customer(customer_id),

    CONSTRAINT fk_product
        FOREIGN KEY(product_id)
        REFERENCES dim_product(product_id),

    CONSTRAINT fk_store
        FOREIGN KEY(store_id)
        REFERENCES dim_store(store_id),

    CONSTRAINT fk_date
        FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id)
);

-- =====================================================
-- FILE TRACKING
-- =====================================================

CREATE TABLE IF NOT EXISTS processed_files (
    file_name VARCHAR(255) PRIMARY KEY,
    processed_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);