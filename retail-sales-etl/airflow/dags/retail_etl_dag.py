from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "retail_sales_etl",
    start_date = datetime(2025, 1, 1),
    schedule = "@daily",
    catchup = False,
    tags = ["retail", "etl"]
) as dag:
    
    run_pipeline = BashOperator(
        task_id = "run_pipeline",
        bash_command = "python /opt/airflow/etl/run_pipeline.py"
    )








