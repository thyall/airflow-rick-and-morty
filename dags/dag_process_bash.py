from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Definindo argumentos padrão para a DAG
default_args = {
    'owner': 'user',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Criando a DAG
dag = DAG(
    'dag_with_bash_operator_and_logging',
    default_args=default_args,
    description='DAG para rodar um script Python usando BashOperator',
    schedule_interval=timedelta(days=1),
)

# Definindo a tarefa com BashOperator
run_script_task = BashOperator(
    task_id='run_script_task',
    bash_command=(
        'python3 /opt/airflow/scripts/texto.py'  # Executa o script e redireciona os logs
    ),
    dag=dag,
)

# Se precisar de outras tasks, você pode encadeá-las aqui
# ex: run_script_task >> other_task
