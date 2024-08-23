import subprocess  # Módulo para rodar comandos no sistema
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Função que executa o script Python dentro de um ambiente virtual
def run_script_in_virtualenv():
    # Utilizando subprocess para rodar o comando no shell
    # A função source ativa o ambiente virtual e, em seguida, o script Python é executado
    subprocess.run(
        'python /opt/airflow/scripts/seu_script.py',
        shell=True,  # Necessário para permitir o uso de `source`
        check=True  # Se o comando falhar, uma exceção será lançada
    )

# Definindo argumentos padrão para a DAG
default_args = {
    'owner': 'user',  # Proprietário da DAG
    'start_date': datetime(2024, 8, 22),  # Data de início da DAG
    'retries': 1,  # Número de tentativas de retry em caso de falha
}

# Criando a DAG
dag = DAG(
    'run_python_script_in_virtualenv',  # Nome da DAG
    default_args=default_args,  # Argumentos padrão
    schedule_interval=None,  # A DAG não será executada em um intervalo regular (manual)
)

# Tarefa que executa a função Python
run_python_script = PythonOperator(
    task_id='run_python_script',  # Identificador único da tarefa
    python_callable=run_script_in_virtualenv,  # Função Python a ser chamada
    dag=dag,  # Associa a tarefa à DAG
)

# Definição da DAG com apenas uma tarefa
