import sqlite3
from exibir_menu import exibir_menu

# Função para iniciar o sistema
def iniciar_sistema():
    # Conectar ao banco de dados no diretório correto
    conn = sqlite3.connect('data/livraria.db')  # Certifique-se de que o caminho está correto
    return conn

if __name__ == '__main__':
    conn = iniciar_sistema()

    try:
        exibir_menu(conn)  # Passa a conexão para o menu
    finally:
        conn.close()  # Fecha a conexão quando sair do sistema
