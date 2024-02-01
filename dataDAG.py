from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from dataEtl import runEtl

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 28),
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

with DAG(
    dag_id='project_dag',
    default_args=default_args,
    description='my first etl',
    schedule_interval='@daily'
):

    run_etl = PythonOperator(
        task_id = 'project_etl',
        python_callable=runEtl,
    )

run_etl