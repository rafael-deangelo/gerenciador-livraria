import os

from criar_backup import criar_backup, limpar_backups_antigos
from crud_livros import adicionar_livro, listar_livros, atualizar_preco, remover_livro, buscar_livros_por_autor, cursor
from exportar_excel import exportar_para_excel
from importar_excel import importar_de_excel
from relatorios_html import gerar_relatorio_html
from relatorios_pdf import gerar_relatorio_pdf
from relatorios_word import gerar_relatorio_word


def verificar_diretorio_relatorios():
    caminho_diretorio = 'C:\\Users\\WILLIAN\\PycharmProjects\\Gerenciador_Livraria\\relatorios'
    if not os.path.exists(caminho_diretorio):
        os.makedirs(caminho_diretorio)
        print(f"Diretório de relatórios criado: {caminho_diretorio}")
    return caminho_diretorio


def exibir_menu(conn):
    while True:
        print("\nMenu Principal:")
        print("1. Adicionar novo livro")
        print("2. Exibir todos os livros")
        print("3. Atualizar preço de um livro")
        print("4. Remover um livro")
        print("5. Buscar livros por autor")
        print("6. Exportar dados para Excel")
        print("7. Importar dados de Excel")
        print("8. Fazer backup do banco de dados")
        print("9. Limpar backups antigos")
        print("10. Gerar Relatório em PDF")
        print("11. Gerar Relatório em HTML")
        print("12. Gerar Relatório em DOCX")
        print("0. Sair")

        escolha = input("Escolha uma opção: ").strip()  # Remove espaços em branco

        if escolha == '1':
            # Adiciona um novo livro
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")

            # Validação para o ano de publicação
            while True:
                try:
                    ano_publicacao = int(input("Ano de publicação: "))
                    break  # Sai do loop se o valor for válido
                except ValueError:
                    print("Ano de publicação inválido. Por favor, insira um número inteiro válido.")

            # Validação para o preço do livro
            while True:
                try:
                    preco = input("Preço do livro: ").replace(',', '.')  # Substituir vírgula por ponto
                    preco = float(preco)  # Converter para float
                    break  # Sai do loop se o valor for válido
                except ValueError:
                    print("Preço inválido. Por favor, insira um número válido.")

            adicionar_livro(titulo, autor, ano_publicacao, preco)

        elif escolha == '2':
            # Lista todos os livros
            listar_livros()

        elif escolha == '3':
            # Atualiza o preço de um livro
            id_livro = int(input("ID do livro para atualizar: "))
            while True:
                try:
                    novo_preco = input("Novo preço do livro: ").replace(',', '.')  # Substituir vírgula por ponto
                    novo_preco = float(novo_preco)  # Converter para float
                    break
                except ValueError:
                    print("Preço inválido. Por favor, insira um valor numérico válido.")
            atualizar_preco(id_livro, novo_preco)

        elif escolha == '4':
            # Remove um livro
            id_livro = int(input("ID do livro para remover: "))
            remover_livro(id_livro)

        elif escolha == '5':
            # Busca livros por autor
            autor = input("Nome do autor: ")
            buscar_livros_por_autor(autor)

        elif escolha == '6':
            # Exporta dados para Excel
            exportar_para_excel('C:\\Users\\WILLIAN\\PycharmProjects\\Gerenciador_Livraria\\exports\\livros_exportados.xlsx', conn)

        elif escolha == '7':
            # Importa dados de Excel
            caminho_excel = 'C:\\Users\\WILLIAN\\PycharmProjects\\Gerenciador_Livraria\\exports\\livros_exportados.xlsx'
            if caminho_excel:
                importar_de_excel(caminho_excel)
            else:
                print("Nenhum arquivo foi selecionado.")

        elif escolha == '8':
            # Faz backup do banco de dados
            criar_backup()

        elif escolha == '9':
            # Limpa backups antigos
            limpar_backups_antigos()

        elif escolha == '10':
            # Gera relatório em PDF
            verificar_diretorio_relatorios()
            cursor.execute('SELECT * FROM livros')
            livros = cursor.fetchall()
            caminho_pdf = 'C:\\Users\\WILLIAN\\PycharmProjects\\Gerenciador_Livraria\\relatorios\\relatorio_livros.pdf'
            gerar_relatorio_pdf(livros, caminho_pdf)

        elif escolha == '11':
            # Gera relatório em HTML
            verificar_diretorio_relatorios()
            cursor.execute('SELECT * FROM livros')
            livros = cursor.fetchall()
            caminho_html = 'C:\\Users\\WILLIAN\\PycharmProjects\\Gerenciador_Livraria\\relatorios\\relatorio_livros.html'
            gerar_relatorio_html(livros, caminho_html)

        elif escolha == '12':
            # Gera relatório em Word
            cursor.execute('SELECT * FROM livros')
            livros = cursor.fetchall()
            caminho_word = 'C:\\Users\\WILLIAN\\PycharmProjects\\Gerenciador_Livraria\\relatorios\\relatorio_livros.docx'
            gerar_relatorio_word(livros, caminho_word)

        elif escolha == '0':
            # Encerra o sistema
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")
