"""
primeira DAG v2: hello world
"""

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


@dag(
    start_date=datetime(2024, 11, 14),
    schedule="@daily",
    doc_md=__doc__,
)
def a_primeira_DAG_v2():
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="hello", bash_command="echo hello world")
    end = EmptyOperator(task_id="end")
    start >> hello >> end


criar_DAG = a_primeira_DAG_v2()
