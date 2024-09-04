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

# Documentação do Projeto `airflow-poc`

## Estrutura Geral do Projeto

### config/
- **Descrição:** Diretório utilizado para armazenar arquivos de configuração do projeto.
- **Propósito:** Centraliza as configurações necessárias para a execução do projeto, como arquivos de configuração do Airflow, Docker, ou outros componentes.

### dags/
- **Descrição:** Diretório onde as DAGs (Directed Acyclic Graphs) do Airflow são armazenadas. As DAGs definem as tarefas e suas dependências.
- **Principais Arquivos:**
  - `dag_process.py`, `dag_process_bash.py`, `dag_rick_and_morty_simplificada.py`, `dag_tutorial.py`: Scripts Python que definem as DAGs específicas para diferentes processos.
- **Propósito:** Organiza e executa os diferentes fluxos de trabalho automatizados no Airflow.

### data/
- **Descrição:** Diretório utilizado para armazenar dados persistentes que são usados ou gerados pelos processos.
- **Principais Arquivos:**
  - `character.json`, `episode.json`, `location.json`: Arquivos JSON que provavelmente contêm dados obtidos de APIs ou outras fontes de dados.
  - `meu_arquivo.txt`: Arquivo de texto genérico que pode ser usado por algum script ou processo.
- **Propósito:** Serve como repositório central para os dados que os processos de ETL (Extração, Transformação e Carga) manipulam.

### docker-compose.yaml
- **Descrição:** Arquivo de configuração do Docker Compose, utilizado para definir e executar múltiplos contêineres Docker.
- **Propósito:** Facilita a orquestração dos diferentes serviços necessários para o projeto, como o Airflow, PostgreSQL, Redis, etc.

### logs/
- **Descrição:** Diretório onde os logs das execuções das DAGs e do scheduler do Airflow são armazenados.
- **Subdiretórios Importantes:**
  - `dag_id=dag_with_bash_operator_and_logging/`: Contém logs específicos para DAGs que utilizam o operador Bash.
  - `scheduler/`: Armazena logs relacionados ao scheduler do Airflow.
  - `dag_processor_manager/`: Logs do gerenciador de processamento de DAGs.
- **Propósito:** Fornece informações detalhadas sobre a execução das tarefas, útil para depuração e monitoramento.

### opt/airflow/
- **Descrição:** Diretório utilizado principalmente para salvar dados na pasta `DATA`, com o intuito de replicação ou armazenamento de dados externos.
- **Propósito:** Centraliza dados que precisam ser replicados ou armazenados externamente, garantindo que estejam disponíveis para processos do Airflow ou outros fins.

### plugins/
- **Descrição:** Diretório reservado para plugins do Airflow.
- **Propósito:** Permite a extensão das funcionalidades do Airflow com componentes personalizados.

### src/
- **Descrição:** Diretório onde são armazenados arquivos e códigos externos que serão executados via Airflow.
- **Propósito:** Organiza os scripts que serão executados pelo Airflow utilizando PythonOperator ou BashOperator, podendo conter desde arquivos isolados até projetos completos.

## Diretório do projeto (simplificado)
```plaintext
├── README.md
├── config
├── dags
│   ├── __pycache__
│   ├── dag_process.py
│   ├── dag_process_bash.py
│   ├── dag_rick_and_morty_simplificada.py
│   └── dag_tutorial.py
├── data
├── docker-compose.yaml
├── logs
│   ├── dag_id=dag_with_bash_operator_and_logging
│   ├── dag_id=rick_and_morty_dag
│   ├── dag_id=run_python_script_in_virtualenv
│   ├── dag_id=simplified_rick_and_morty_dag
│   ├── dag_processor_manager
│   │   └── dag_processor_manager.log
│   ├── scheduler
│   │   ├── 2024-08-01
│   │   │   └── native_dags
│   │   │       └── example_dags
├── opt
│   └── airflow
│       ├── config
│       ├── dags
│       ├── data
│       │   ├── character.json
│       │   ├── episode.json
│       │   ├── location.json
│       │   └── meu_arquivo.txt
│       ├── logs
│       ├── plugins
│       └── scripts
│           └── texto.py
├── plugins
├── requirements.txt
└── src
    └── teste.py
``` 

## Autor
Thyall D`greville
