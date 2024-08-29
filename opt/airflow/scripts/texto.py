OUTPUT_DIR = '/opt/airflow/data/'

# Nome do arquivo que será criado
nome_do_arquivo = 'meu_arquivo'

# Frase que será escrita no arquivo
frase = 'Esta é a frase que será escrita no arquivo.'

# Abrir o arquivo no modo de escrita ('w')
with open(f'{OUTPUT_DIR}{nome_do_arquivo}.txt', 'w') as f:
    # Escrever a frase no arquivo
    f.write(frase)

print(f"O arquivo '{nome_do_arquivo}' foi criado e a frase foi escrita com sucesso.")
