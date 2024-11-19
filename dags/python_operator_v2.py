from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.decorators import task
import pendulum
import pprint


with DAG(
    dag_id="python_operator_v2",
    schedule="* * * * *",
    start_date=pendulum.datetime(2024, 11, 18, 10, 40, tz="America/Sao_Paulo"),
    catchup=True,
) as dag:
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    @task(task_id="python")
    def meu_codigo(ds=None, **kwargs):
        pprint.pprint(kwargs)
        print(ds)
        return "meu retorno agora é este texto"

    python = meu_codigo()

start >> python >> end