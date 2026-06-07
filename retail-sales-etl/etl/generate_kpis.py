import pandas as pd
from db import get_engine

def generate_kpis():

    engine = get_engine()

    queries = {

        "total_revenue": """
        SELECT
            ROUND(SUM(total_amount), 2)
            AS total_revenue
        FROM fact_sales
        """,

        "daily_revenue": """
        SELECT 
            date_id,
            ROUND(SUM(total_amount), 2)
            AS revenue
        FROM fact_sales
        GROUP BY date_id
        ORDER BY date_id
        """,

        "top_products": """
        SELECT 
            product_id,
            ROUND(SUM(total_amount), 2)
            AS revenue
        FROM fact_sales
        GROUP BY product_id
        ORDER BY revenue DESC
        LIMIT 10
        """,

        "revenue_by_region": """
        SELECT 
            ds.region,
            ROUND(SUM(fs.total_amount), 2)
            AS revenue
        FROM fact_sales fs
        JOIN dim_store ds
        ON fs.store_id = ds.store_id
        GROUP BY ds.region
        ORDER BY REVENUE DESC
        """
    }

    for kpi_name, query in queries.items():

        df = pd.read_sql(query, engine)

        print(f"\n==== {kpi_name.upper()} ====\n")

        print(df)

if __name__ == "__main__":
    generate_kpis()






