from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import pendulum
import pprint


def meu_codigo(**kwargs):
    print("nieremberg")
    pprint.pprint(kwargs)
    return 123


with DAG(
    dag_id="python_operator_v1",
    schedule="* * * * *",
    start_date=pendulum.datetime(2024, 11, 18, 10, 40, tz="America/Sao_Paulo"),
    catchup=True,
) as dag:
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")
    python = PythonOperator(task_id="python", python_callable=meu_codigo)

start >> python >> end
