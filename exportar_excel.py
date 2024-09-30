import pandas as pd
import sqlite3
from pathlib import Path

def exportar_para_excel(caminho_excel, conn):
    # Verifica se a conexão está aberta
    if conn is None:
        print("Erro: A conexão com o banco de dados está fechada.")
        return

    # Cria um cursor para executar consultas SQL
    cursor = conn.cursor()

    # Seleciona todos os dados da tabela 'livros'
    cursor.execute('SELECT * FROM livros')
    dados = cursor.fetchall()

    # Cria um DataFrame a partir dos dados
    colunas = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(dados, columns=colunas)

    # Extrai o diretório do caminho do arquivo
    diretorio_exportacao = Path(caminho_excel).parent

    # Cria o diretório se não existir
    diretorio_exportacao.mkdir(parents=True, exist_ok=True)

    # Exporta os dados para um arquivo Excel
    df.to_excel(caminho_excel, index=False)
    print(f"Dados exportados com sucesso para {caminho_excel}")

    # Fecha o cursor
    cursor.close()
