import requests
import json
import pandas as pd

BASE_URL = "https://rickandmortyapi.com/api/"

# Função para extrair dados da API e salvar em arquivos JSON
def extract_and_save():

    endpoints = ["character", "location", "episode"]
    
    # Configuração de logging
    print("Iniciando a extração dos dados da API Rick and Morty")

    for endpoint in endpoints:
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            with open(f'/home/thyall/datalake-airflow/bronze/{endpoint}.json', 'w') as f:
                json.dump(data, f)
            print(f"Dados do endpoint {endpoint} salvos com sucesso.")
        else:
            print(f"Falha ao extrair dados do endpoint {endpoint}. Status Code: {response.status_code}")

# Função para ler os arquivos JSON e imprimir o conteúdo como DataFrame
def read_and_print():
    endpoints = ["character", "location", "episode"]
    
    for endpoint in endpoints:
        try:
            with open(f'/home/thyall/datalake-airflow/bronze/{endpoint}.json', 'r') as f:
                data = json.load(f)
                df = pd.json_normalize(data['results'])
                # logging.info(f"Primeiros registros do endpoint {endpoint}:")
                print(f"Primeiros registros do endpoint {endpoint}:")
                # logging.info(df.head())
                print(df.head())
        except FileNotFoundError:
            print(f"Arquivo JSON para o endpoint {endpoint} não encontrado.")

extract_and_save()