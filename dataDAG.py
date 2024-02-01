from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from dataEtl import runEtl
from saveToDB import saveToDBFunc

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
    #Fetch data/ save file in s3 bucket
    run_etl = PythonOperator(
        task_id = 'project_etl',
        python_callable=runEtl,
    )

    #save data in aws DB
    saveDataDB= PythonOperator(
        task_id='save_to_db',
        python_callable=
    )

run_etl