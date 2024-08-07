# Airflow Rick and Morty DAG

Este repositório contém uma DAG do Airflow que busca dados da API do Rick and Morty, salva em arquivos JSON, e imprime os dados usando Pandas DataFrame.

## Resumo sobre Airflow

Apache Airflow é uma plataforma de código aberto para criar, agendar e monitorar fluxos de trabalho programáveis. Com Airflow, você define seus fluxos de trabalho como código Python, o que facilita a automação de tarefas complexas.

### Conceitos Importantes

- **DAG (Directed Acyclic Graph)**: Um DAG é uma coleção de todas as tarefas que você deseja executar, organizadas de uma maneira que reflita suas relações e dependências. No Airflow, uma DAG é definida como um script Python.
- **Operator**: Operadores são blocos de construção fundamentais de uma DAG. Cada operador é uma unidade de trabalho, como executar uma função Python, rodar um script Bash, ou transferir dados.
- **Task**: Uma instância de um Operator que é executada como parte de uma DAG.
- **Task Instance**: A execução de uma Task em um determinado ponto no tempo.
- **Scheduler**: O componente do Airflow que distribui tarefas para os Workers.
- **Executor**: A configuração que determina como as tasks serão executadas (por exemplo, LocalExecutor, CeleryExecutor).

## O que é Docker Compose?

Docker Compose é uma ferramenta para definir e gerenciar aplicativos Docker multi-containers. Com Docker Compose, você usa um arquivo YAML para configurar os serviços da sua aplicação e, em seguida, com um único comando, pode criar e iniciar todos os serviços.

## Estrutura do Projeto

- `dags/simplified_rick_and_morty_dag.py`: Código da DAG simplificada.
- `Dockerfile`: Arquivo Docker para instalar dependências adicionais (não necessário para a execução atual).
- `docker-compose.yml`: Arquivo de configuração do Docker Compose.
- `logs/`: Diretório para logs do Airflow.
- `plugins/`: Diretório para plugins do Airflow.

## Requisitos

### Instalação do Docker

1. **Atualize o índice de pacotes do sistema**:
   ```bash
   sudo apt-get update
