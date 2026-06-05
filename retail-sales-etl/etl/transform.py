import pandas as pd
from datetime import datetime

def remove_duplicates(df):
    return df.drop_duplicates()

def remove_invalid_records(df):
    
    df = df[df["customer_id"].notna()]

    df = df[df["quantity"] >= 0]                    

    df = df[df["unit_price"] >= 0]
    
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors = "coerce"
    )

    df = df[df["order_date"].notna()]

    return df

def standardize_dates(df): 
    df["order_date"] = pd.to_datetime(
        df["order_date"]
    )

    df["order_date"] = df["order_date"].dt.strftime(
        "%Y-%m-%d"
    )

    return df


def create_total_amount(df):

    df["total_amount"] = df["quantity"] * df["unit_price"]

    return df

def add_load_timestamp(df):

    df["load_timestamp"] = datetime.now()

    return df

def transform_data(df):

    df = remove_duplicates(df)

    df = remove_invalid_records(df)

    df = standardize_dates(df)

    df = create_total_amount(df)

    df = add_load_timestamp(df)

    return df





