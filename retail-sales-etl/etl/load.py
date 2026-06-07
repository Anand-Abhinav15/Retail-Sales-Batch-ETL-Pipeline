from db import get_engine
import pandas as pd

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

    with engine.begin() as conn:

        for _, row in stores.iterrows():

            conn.exec_driver_sql(
                f"""
                INSERT INTO
                dim_store (store_id, region) 
                VALUES ({int(row['store_id'])}, '{row['region']}')
                ON CONFLICT(store_id)
                DO NOTHING;
                """
            )


def load_dim_date(df):

    engine = get_engine()

    dates = (
        df[['order_date']].drop_duplicates()
    )

    with engine.begin() as conn:

        for _, row in dates.iterrows():

            date_value = pd.to_datetime(row["order_date"])

            year = int(date_value.year)
            month = int(date_value.month)
            day = int(date_value.day)
            quarter = int(date_value.quarter)

            conn.exec_driver_sql(
                f"""
                INSERT INTO 
                dim_date (date_id, year, month, day, quarter)
                VALUES (
                    '{date_value.strftime("%Y-%m-%d")}',
                    {year},
                    {month},
                    {day},
                    {quarter}
                )
                ON CONFLICT(date_id)
                DO NOTHING
                """
            )


def load_dimensions(df):

    load_dim_customer(df)

    load_dim_product(df)

    load_dim_store(df)

    load_dim_date(df)

    print("Dimensions loaded successfully!!")



