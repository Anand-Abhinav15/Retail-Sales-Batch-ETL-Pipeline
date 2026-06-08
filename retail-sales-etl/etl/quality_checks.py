import pandas as pd
from db import get_engine

def run_quality_checks():

    engine = get_engine()

    checks = {

        "fact_sales_count":
        """
        SELECT COUNT(*) AS cnt
        FROM fact_sales
        """,

        "null_customer_check":
        """
        SELECT COUNT(*) AS cnt
        FROM fact_sales
        WHERE customer_id IS NULL
        """,

        "negative_sales":
        """
        SELECT COUNT(*) AS cnt
        FROM fact_sales
        WHERE total_amount < 0
        """
    }

    for name, query in checks.items():

        result = pd.read_sql(query, engine)

        print(f"\n{name}")

        print(result)


if __name__ == "__main__":
    run_quality_checks()





