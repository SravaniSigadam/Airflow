"""Example DAG demonstrating the usage of the PythonOperator."""
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from textwrap import dedent


with DAG(
    dag_id='example_ML_pipeline_DAG',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['my_implementation'],
) as dag:
    training_task = BashOperator(
        task_id='training_task',
        bash_command='python ~/PycharmProjects/Airflow/ModelScript.py',
        dag=dag
    )
    scoring_task = BashOperator(
        task_id='scoring_task',
        bash_command='python ~/PycharmProjects/Airflow/SampleScript.py',
        dag=dag
    )
    training_task.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)

    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG
    dag.doc_md = """
        This is a documentation placed anywhere
        """  # otherwise, type it like this
    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
    """
    )
    training_task >> scoring_task
