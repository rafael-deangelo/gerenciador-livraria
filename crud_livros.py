import sqlite3
from criar_backup import criar_backup

# Conexão com o banco de dados
conn = sqlite3.connect('data/livraria.db')  # Certifique-se de que este caminho está correto
cursor = conn.cursor()


# Adicionar um Novo Livro
def adicionar_livro(titulo, autor, ano_publicacao, preco):
    cursor.execute('''
            INSERT INTO livros (titulo, autor, ano_publicacao, preco)
            VALUES (?, ?, ?, ?)
        ''', (titulo, autor, ano_publicacao, preco))

    conn.commit()
    print(f'Livro "{titulo}" adicionado com sucesso!')

    # Criar backup após adicionar livro
    criar_backup()


# Fechar a conexão depois de adicionar os dados (normalmente feito no final do programa)
# conn.close()

# Exibir Todos os Livros
def listar_livros():
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    if livros:
        for livro in livros:
            print(f'ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Preço: R$ {livro[4]:.2f}')
    else:
        print('Nenhum livro encontrado.')


# Atualizar o Preço de um Livro
def atualizar_preco(id_livro, novo_preco):
    cursor.execute('''
            UPDATE livros
            SET preco = ?
            WHERE id = ?
        ''', (novo_preco, id_livro))

    if cursor.rowcount > 0:
        conn.commit()
        print(f'Preço do livro de ID {id_livro} atualizado para R$ {novo_preco:.2f}.')
        # Criar backup após atualização
        criar_backup()
    else:
        print(f'Nenhum livro encontrado com o ID {id_livro}.')


# Remover um Livro
def remover_livro(id_livro):
    cursor.execute('DELETE FROM livros WHERE id = ?', (id_livro,))

    if cursor.rowcount > 0:
        conn.commit()
        print(f'Livro de ID {id_livro} removido com sucesso.')
        # Criar backup após remoção
        criar_backup()
    else:
        print(f'Nenhum livro encontrado com o ID {id_livro}.')


# Buscar Livros por Autor
def buscar_livros_por_autor(autor):
    cursor.execute('SELECT * FROM livros WHERE autor LIKE ?', ('%' + autor + '%',))
    livros = cursor.fetchall()

    if livros:
        for livro in livros:
            print(f'ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Preço: R$ {livro[4]:.2f}')
    else:
        print(f'Nenhum livro encontrado para o autor "{autor}".')


# Adicionado para evitar que duplique livros na importação
def buscar_livro_por_titulo(titulo):
    cursor.execute("SELECT * FROM livros WHERE titulo = ?", (titulo,))  # Use o nome correto da coluna
    return cursor.fetchone() is not None  # Retorna True se o livro existir, False caso contrário