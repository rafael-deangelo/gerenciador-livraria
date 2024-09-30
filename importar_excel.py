import pandas as pd
from crud_livros import adicionar_livro, buscar_livro_por_titulo


def importar_de_excel(caminho_excel):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_excel)

    # Iterar sobre as linhas do DataFrame
    livros_importados = 0
    for index, linha in df.iterrows():
        titulo = linha['titulo']
        autor = linha['autor']
        ano_publicacao = int(linha['ano_publicacao'])
        preco = float(linha['preco'])

        # Verificar se o livro já existe
        if not buscar_livro_por_titulo(titulo):
            adicionar_livro(titulo, autor, ano_publicacao, preco)  # Reutilizamos a função de adicionar
            livros_importados += 1
        else:
            print(f'O livro "{titulo}" já existe no banco de dados. Não será adicionado.')

    print(f'{livros_importados} livros importados do arquivo Excel.')
