from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.models.connection import Connection
from airflow.utils.session import create_session
import os
import json
import subprocess

default_args = {
    'owner': 'datnt309',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='etl_anime_data',
    default_args=default_args,
    description='A DAG to process anime data',
    schedule_interval=None,
)

def transform_csv():
    subprocess.run(["python", "/opt/airflow/dags/transform.py"])

transform_task = PythonOperator(
    task_id='transform_csv',
    python_callable=transform_csv,
    dag=dag,
)

# Upload file anime_modified.csv lên S3
upload_task = LocalFilesystemToS3Operator(
    task_id='upload_anime_modified_csv',
    filename=r'/opt/airflow/output/Top_Anime_data_output.csv',
    dest_key='Top_Anime_data_output.csv',
    dest_bucket='datnt309',
    aws_conn_id='aws_connection',
    replace=True,
    dag=dag,
)

# Define task dependencies
transform_task >> upload_task

