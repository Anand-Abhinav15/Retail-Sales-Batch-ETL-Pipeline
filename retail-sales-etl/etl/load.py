from etl.db import get_engine

def load_dim_customer(df):

    engine = get_engine()

    customer = (
        df[["customer_id"]].drop_duplicates()
    )

    with engine.begin() as conn:

        for _, row in customer.iterrows():

            conn.exec_driver_sql(
                f"""
                INSERT INTO dim_customer(customer_id)
                VALUES ({int(row['customer_id'])})
                ON CONFLICT(customer_id)
                DO NOTHING;
                """
            )
                

def load_dim_product(df):

    engine = get_engine()

    products = (
        df[["product_id"]].drop_duplicates()
    )

    with engine.begin() as conn:

        for _, row in products.iterrows():

            conn.exec_driver_sql(
                f"""
                INSERT INTO dim_product(product_id)
                VALUES ({int(row['product_id'])})
                ON CONFLICT(product_id)
                DO NOTHING;
                """
            )

def load_dim_store(df):
     
    engine = get_engine()

    stores = (
         df[["store_id", "region"]].drop_duplicates()
    )

    with engine.begin() as conn:s






