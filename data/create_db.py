import sqlite3  # Módulo para Gerenciar o Banco de Dados
from pathlib import Path

# Criando diretório 'data' se não existir
Path('data').mkdir(parents=True, exist_ok=True)

# Conexão com o banco de dados (ou criação se não existir)
conexao = sqlite3.connect('data/livraria.db')  # Alterado para incluir 'data/'
cursor = conexao.cursor()

# Criando a tabela de livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL,
    preco REAL NOT NULL
)
''')

# Confirmando a criação da tabela
conexao.commit()

# Fechando a conexão
conexao.close()

print("Banco de dados e tabela 'livros' criados com sucesso!")
