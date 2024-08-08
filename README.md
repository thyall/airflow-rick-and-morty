# Airflow Rick and Morty DAG

Este repositório contém DAGs do Airflow que buscam dados da API do Rick and Morty, salva em arquivos JSON, e imprime os dados usando Pandas DataFrame. Tem como intuito servir de modelo de infraestrutura e de criação de DAGs

## O que é Docker Compose?

Docker Compose é uma ferramenta para definir e gerenciar aplicativos Docker multi-containers. Com Docker Compose, você usa um arquivo YAML para configurar os serviços da sua aplicação e, em seguida, com um único comando, pode criar e iniciar todos os serviços.

## Resumo sobre Airflow

Apache Airflow é uma plataforma de código aberto para criar, agendar e monitorar fluxos de trabalho programáveis. Com Airflow, você define seus fluxos de trabalho como código Python, o que facilita a automação de tarefas complexas.

### Conceitos Importantes

- **DAG (Directed Acyclic Graph)**: Um DAG é uma coleção de todas as tarefas que você deseja executar, organizadas de uma maneira que reflita suas relações e dependências. No Airflow, uma DAG é definida como um script Python.
- **Operator**: Operadores são blocos de construção fundamentais de uma DAG. Cada operador é uma unidade de trabalho, como executar uma função Python, rodar um script Bash, ou transferir dados.
- **Task**: Uma instância de um Operator que é executada como parte de uma DAG.
- **Task Instance**: A execução de uma Task em um determinado ponto no tempo.
- **Scheduler**: O componente do Airflow que distribui tarefas para os Workers.
- **Executor**: A configuração que determina como as tasks serão executadas (por exemplo, LocalExecutor, CeleryExecutor).

## Estrutura do Projeto

- `dags/dag_rick_and_morty_simplificada.py`: Código da DAG simplificada.
- `Dockerfile`: Arquivo Docker para instalar dependências adicionais (não necessário para a execução atual).
- `docker-compose.yml`: Arquivo de configuração do Docker Compose.
- `logs/`: Diretório para logs do Airflow.
- `plugins/`: Diretório para plugins do Airflow.

## Requisitos

- Python
- Docker compose
- Virtual env

### Instalação do Docker

1. **Atualize o índice de pacotes do sistema**:
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   ```

2. **Baixe a versão estável atual do Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

   # etapa não obrigatória
   sudo chmod +x /usr/local/bin/docker-compose

   docker-compose --version
    ```
### Instalação Python e Ambiente virtual

1. **Instale o Python 3 e venv**:
   ```bash
   sudo apt-get install python3 python3-venv python3-pip
    ```
2. **Crie Ambiente virtua**:
   ```bash
      python3 -m venv airflow_env
   ```
3. **Instale dependências**:
    ```bash
    # se necessario
    pip install -r requirements.txt
   ```

## Passo a Passo para Instalação
### Requisitos
- Ambiente Linux (ou WSL2)
- Docker e Docker Compose instalados.
- Python e ambiente virtual configurados.

### Passos
1. Clone este repositório:

   ```bash
   git clone https://github.com/SEU_USUARIO/airflow-rick-and-morty.git
   cd airflow-rick-and-morty
     ``` 
2. Inicie os containers Docker:
   ```bash
   docker-compose up -d
   ```
3. Acesse a interface web do Airflow:

Abra seu navegador e vá para http://localhost:8080.
As credenciais padrão são airflow para ambos username e password.
Ative e execute a DAG:

Na interface do Airflow, encontre a DAG simplified_rick_and_morty_dag.
Ative a DAG clicando no botão "Off" para mudá-lo para "On".
Execute a DAG manualmente clicando no botão "Trigger DAG".


### Principais Comandos
1. Subir containers:
   ```bash
   docker-compose up -d
   ```

2. Desligar containers:
   ```bash
   docker-compose down
   ```
2. Analisar containers:
   ```bash
   docker ps
   ```

4. Ver logs de um container:
   ```bash
   docker-compose logs <nome_do_serviço>
   ```
### Explicação das Tarefas na DAG
Extrair e Salvar Dados:

- Extrai dados de três endpoints da API Rick and Morty.
- Salva os dados em arquivos JSON.

Ler e Imprimir Dados:

- Lê os arquivos JSON salvos.
- Converte os dados para um DataFrame Pandas e imprime os primeiros registros no terminal.

## Autor
Thyall D`greville
