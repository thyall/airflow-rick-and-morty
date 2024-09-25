from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Definindo argumentos padrão para a DAG
default_args = {
    'owner': 'Mineracao',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 15),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Criando a DAG
dag = DAG(
    'dag_with_bash_operator_mining',
    default_args=default_args,
    description='DAG para rodar um script Python usando BashOperator para mineracao',
    schedule_interval=timedelta(days=1),
)


# Definindo a tarefa com BashOperator
activate_venv = BashOperator(
    task_id='activate_venv',
    bash_command=(
        'source /opt/airflow/enviroments/.env/bin/activate'
    ),
    dag=dag,
)

# Definindo a tarefa com BashOperator
run_crawler_blogs = BashOperator(
    task_id='run_crawler_blogs',
    bash_command=(
        'python3 /opt/airflow/scripts/crawler_blogs_rss.py'
    ),
    dag=dag,
)

activate_venv >> run_crawler_blogs
