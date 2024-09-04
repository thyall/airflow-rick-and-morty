from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Definindo argumentos padrão para a DAG
default_args = {
    'owner': 'user',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 28),
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

#'source /opt/airflow/scripts/venv/bin/activate && '  # Ativa o ambiente virtual
# 'python /opt/airflow/scripts/texto.py >> /opt/airflow/logs/seu_script.log 2>&1'  # Executa o script e redireciona os logs