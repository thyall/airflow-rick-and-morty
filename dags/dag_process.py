from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import logging

# Configuração básica de logging
logging.basicConfig(
    filename='/opt/airflow/logs/logile.log',  # Arquivo onde os logs serão salvos
    level=logging.INFO,  # Nível do log (INFO, neste caso)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Formato do log
)
logger = logging.getLogger(__name__)  # Obtém um logger para o script

# Definindo a função Python que será executada pela DAG
def executar_script():
    try:
        # Definindo o caminho de saída do arquivo
        output_dir = '/opt/airflow/data/'
        output_file = 'resultado.txt'
        file_path = os.path.join(output_dir, output_file)

        # Garantindo que o diretório de saída exista
        os.makedirs(output_dir, exist_ok=True)
        
        # Escrevendo no arquivo
        with open(file_path, 'w') as file:
            file.write("Este é o conteúdo do arquivo gerado pelo script Python.")
        
        # Logando uma mensagem de sucesso no arquivo e no Airflow
        logger.info(f"Arquivo gerado com sucesso em: {file_path}")
        logging.info(f"Arquivo gerado com sucesso em: {file_path}")  # Essa linha envia o log para o Airflow
    
    except Exception as e:
        # Logando uma mensagem de erro no arquivo e no Airflow
        logger.error(f"Erro ao gerar o arquivo: {e}")
        logging.error(f"Erro ao gerar o arquivo: {e}")  # Essa linha envia o log para o Airflow
        raise  # Relevanta a exceção para que a DAG registre a falha

# Definindo argumentos padrão para a DAG
default_args = {
    'owner': 'user',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 3),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Criando a DAG
dag = DAG(
    'dag_with_python_operator_and_logging',
    default_args=default_args,
    description='DAG para rodar um script Python usando PythonOperator',
    schedule_interval=timedelta(days=1),
)

# Definindo a tarefa com PythonOperator
run_script_task = PythonOperator(
    task_id='run_script_task',
    python_callable=executar_script,  # Função Python a ser executada
    dag=dag,
)

# Encadeamento de tarefas, se houver mais tarefas
# ex: run_script_task >> another_task

