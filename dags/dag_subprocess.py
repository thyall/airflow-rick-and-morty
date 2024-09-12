from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import logging
import subprocess

# Definindo as configurações do logger
logging.basicConfig(
    filename='/caminho/no/container/X/seu_script.log',  # Local onde o log será salvo
    level=logging.INFO,  # Nível de log: INFO, ERROR, etc.
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato do log
)

def run_script_in_virtualenv():
    """
    Função para executar um script Python em um ambiente virtual dentro de um container Docker.
    Captura a saída e os erros e os loga em um arquivo de log.
    """
    try:
        # Comando para ativar o ambiente virtual e rodar o script Python
        result = subprocess.run(
            'python /opt/airflow/scripts/texto.py',
            shell=True,
            capture_output=True,  # Captura stdout e stderr
            text=True,  # Converte a saída para string
            check=True  # Lança uma exceção se o comando retornar um erro
        )
        
        # Logando a saída do script
        logging.info(f"Script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        # Logando erros que ocorreram durante a execução
        logging.error(f"Script failed with error: {e.stderr}")
        # Propaga a exceção para falhar a task no Airflow
        raise

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
    'dag_with_python_operator_and_logging',
    default_args=default_args,
    description='DAG para rodar um script Python com captura de logs',
    schedule_interval=timedelta(days=1),
)

# Criando a tarefa com PythonOperator
run_script_task = PythonOperator(
    task_id='run_script_task',
    python_callable=run_script_in_virtualenv,  # Função a ser executada
    dag=dag,
)

# Se precisar de outras tasks, você pode encadeá-las aqui
# ex: run_script_task >> other_task
