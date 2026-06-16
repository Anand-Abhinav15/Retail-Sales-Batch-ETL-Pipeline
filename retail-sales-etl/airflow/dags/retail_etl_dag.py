from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "abhinav",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id = "retail_sales_etl",
    default_args= default_args,
    start_date = datetime(2025, 1, 1),
    schedule = "@daily",
    catchup = False,
    tags = ["retail", "etl"]
) as dag:
    
    check_files = BashOperator(
        task_id = "check_new_files",
        bash_command = "python /opt/airflow/etl/check_files.py"
    )

    extract_load = BashOperator(
        task_id = "extract_transform_load",
        bash_command = "python /opt/airflow/etl/run_pipeline.py"
    )

    generate_kpis = BashOperator(
        task_id = "generate_kpis",
        bash_command = "python /opt/airflow/etl/generate_kpis.py"
    )

    quality_checks = BashOperator(
        task_id = "quality_checks",
        bash_command = "python /opt/airflow/etl/quality_checks.py"
    )


    check_files >> extract_load >> generate_kpis >> quality_checks
