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



