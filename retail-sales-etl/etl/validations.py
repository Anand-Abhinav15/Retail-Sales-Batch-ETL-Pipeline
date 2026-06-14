import logging 
import pandas as pd

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Validation started")

def validate_nulls(df):
    """
    Check for null values
    """

    null_count = df.isnull().sum().sum()

    if null_count > 0:
        logging.warning(
            f"Found {null_count} null values"
        )

    return int(null_count)

def validate_duplicates(df):
    """
    Check duplicate records
    """

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        logging.warning(
            f"Found {duplicate_count} duplicate rows"
        )

    return int(duplicate_count)

def validate_negative_quantity(df):

    if "quantity" not in df.columns:
        return 0
    
    count = (df["quantity"] < 0).sum()

    if count > 0:
        logging.warning(
            f"Found {count} negative quantities"
        )

    return int(count)

def validate_negative_price(df):

    if "unit_price" not in df.columns:
        return 0
    
    count = (df["unit_price"] < 0).sum()

    if count > 0:
        logging.warning(
            f"Found {count} negative prices"
        )

    return int(count)

def validate_dates(df):

    if "order_date" not in df.columns:
        return 0
    
    converted = pd.to_datetime(
        df["order_date"],
        errors = "coerce"
    )

    invalid_dates = converted.isnull().sum()

    if invalid_dates > 0:
        logging.warning(
            f"Found {invalid_dates} invalid dates"
        )
    
    return int(invalid_dates)

def run_validations(df):

    results = {
        "nulls": validate_nulls(df),
        "duplicates": validate_duplicates(df),
        "negative_quantity": validate_negative_quantity(df),
        "negative_price": validate_negative_price(df),
        "invalid_dates": validate_dates(df)
    }

    return results






