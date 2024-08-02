from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
import requests
import logging
import json

# Configurando o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para fazer requisições à API e lidar com paginação
def fetch_data(endpoint):
    url = f'https://rickandmortyapi.com/api/{endpoint}'
    results = []
    
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results.extend(data['results'])
            url = data['info']['next']
        else:
            logger.error(f'Falha para extrair dados da url: {url}, status code: {response.status_code}')
            break
    
    return results

# Função para salvar os dados em um arquivo JSON
def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f'Dados salvos em {filename}')

# Função para imprimir os dados
def print_data(data):
    logger.info(json.dumps(data, indent=4))
    print(data)

# Funções específicas para cada endpoint com opção de imprimir ou salvar dados
def fetch_characters(save=False):
    data = fetch_data('character')
    if save:
        save_data(data, '/home/thyall/datalake-airflow/bronze/characters.json')
    else:
        print_data(data)
    return 'has_data' if data else 'no_data'

def fetch_episodes(save=False):
    data = fetch_data('episode')
    if save:
        save_data(data, '/home/thyall/datalake-airflow/bronze/episodes.json')
    else:
        print_data(data)
    return 'has_data' if data else 'no_data'

def fetch_locations(save=False):
    data = fetch_data('location')
    if save:
        save_data(data, '/home/thyall/datalake-airflow/bronze/locations.json')
    else:
        print_data(data)
    return 'has_data' if data else 'no_data'

# Funções para branch
def branch_characters(**kwargs):
    return kwargs['task_instance'].xcom_pull(task_ids='fetch_characters')

def branch_episodes(**kwargs):
    return kwargs['task_instance'].xcom_pull(task_ids='fetch_episodes')

def branch_locations(**kwargs):
    return kwargs['task_instance'].xcom_pull(task_ids='fetch_locations')

# Definindo a DAG
default_args = {
    'owner': 'airflow',  # Proprietário da DAG, geralmente o criador ou responsável.
    'depends_on_past': False,  # Se a execução da DAG deve depender do sucesso da execução anterior.
    'start_date': datetime(2024, 8, 1),  # Data inicial da DAG.
    'email_on_failure': False,  # Se deve enviar email em caso de falha.
    'email_on_retry': False,  # Se deve enviar email em caso de tentativa de novo.
    'retries': 1,  # Número de tentativas de re-execução em caso de falha.
    'retry_delay': timedelta(minutes=5),  # Tempo de espera antes de tentar re-executar em caso de falha.
}

dag = DAG(
    'rick_and_morty_dag',
    default_args=default_args,
    description='Uma DAG para extrair dados da API do Rick and Morty',
    schedule_interval=timedelta(days=1),  # Intervalo de agendamento da DAG.
)

# Definindo as tasks
fetch_characters_task = PythonOperator(
    task_id='fetch_characters',
    python_callable=fetch_characters,
    op_kwargs={'save': True},  # Ajuste para salvar dados. Use 'False' para apenas imprimir.
    provide_context=True,
    dag=dag,
)

branch_characters_task = BranchPythonOperator(
    task_id='branch_characters',
    python_callable=branch_characters,
    provide_context=True,
    dag=dag,
)

fetch_episodes_task = PythonOperator(
    task_id='fetch_episodes',
    python_callable=fetch_episodes,
    op_kwargs={'save': True},  # Ajuste para salvar dados. Use 'False' para apenas imprimir.
    provide_context=True,
    dag=dag,
)

branch_episodes_task = BranchPythonOperator(
    task_id='branch_episodes',
    python_callable=branch_episodes,
    provide_context=True,
    dag=dag,
)

fetch_locations_task = PythonOperator(
    task_id='fetch_locations',
    python_callable=fetch_locations,
    op_kwargs={'save': True},  # Ajuste para salvar dados. Use 'False' para apenas imprimir.
    provide_context=True,
    dag=dag,
)

branch_locations_task = BranchPythonOperator(
    task_id='branch_locations',
    python_callable=branch_locations,
    provide_context=True,
    dag=dag,
)

# Dummies para finalizar branches
dummy_has_data = DummyOperator(
    task_id='has_data',
    dag=dag,
)

dummy_no_data = DummyOperator(
    task_id='no_data',
    dag=dag,
)

# Definindo a ordem de execução das tasks
fetch_characters_task >> branch_characters_task >> [dummy_has_data, dummy_no_data]
branch_characters_task >> fetch_episodes_task
fetch_episodes_task >> branch_episodes_task >> [dummy_has_data, dummy_no_data]
branch_episodes_task >> fetch_locations_task
fetch_locations_task >> branch_locations_task >> [dummy_has_data, dummy_no_data]
