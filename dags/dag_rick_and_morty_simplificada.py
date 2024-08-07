from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import requests
import json
import pandas as pd
import logging

BASE_URL = "https://rickandmortyapi.com/api/"

# Função para extrair dados da API e salvar em arquivos JSON
def extract_and_save():

    endpoints = ["character", "location", "episode"]
    
    # Configuração de logging
    logging.info("Iniciando a extração dos dados da API Rick and Morty")

    for endpoint in endpoints:
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            with open(f'/home/thyall/datalake-airflow/bronze/{endpoint}.json', 'w') as f:
                json.dump(data, f)
            logging.info(f"Dados do endpoint {endpoint} salvos com sucesso.")
        else:
            logging.warning(f"Falha ao extrair dados do endpoint {endpoint}. Status Code: {response.status_code}")

# Função para ler os arquivos JSON e imprimir o conteúdo como DataFrame
def read_and_print():
    endpoints = ["character", "location", "episode"]
    
    for endpoint in endpoints:
        try:
            with open(f'/home/thyall/datalake-airflow/bronze/{endpoint}.json', 'r') as f:
                data = json.load(f)
                df = pd.json_normalize(data['results'])
                logging.info(f"Primeiros registros do endpoint {endpoint}:")
                print(f"Primeiros registros do endpoint {endpoint}:")
                logging.info(df.head())
                print(df.head())
        except FileNotFoundError:
            logging.warning(f"Arquivo JSON para o endpoint {endpoint} não encontrado.")

# Definição dos argumentos padrão da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Inicialização da DAG
dag = DAG(
    'simplified_rick_and_morty_dag',
    default_args=default_args,
    description='Uma DAG simplificada para extrair dados da API Rick and Morty, salvar e ler JSONs',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False
)

# Tarefa para extrair e salvar dados
extract_and_save_task = PythonOperator(
    task_id='extract_and_save',
    python_callable=extract_and_save,
    dag=dag,
)

# Tarefa para ler e imprimir dados
read_and_print_task = PythonOperator(
    task_id='read_and_print',
    python_callable=read_and_print,
    dag=dag,
)

# Definição da ordem das tarefas na DAG
extract_and_save_task >> read_and_print_task
