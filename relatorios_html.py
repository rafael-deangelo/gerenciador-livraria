def gerar_relatorio_html(livros, caminho_html):
    html_content = """
    <html>
    <head><title>Relatório de Livros</title></head>
    <body>
    <h1>Relatório de Livros</h1>
    <p>Total de livros: {}</p>
    <table border="1" cellpadding="5" cellspacing="0">
    <tr><th>ID</th><th>Título</th><th>Autor</th><th>Ano</th><th>Preço</th></tr>
    """.format(len(livros))

    for livro in livros:
        html_content += """
        <tr>
            <td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>R$ {:.2f}</td>
        </tr>
        """.format(livro[0], livro[1], livro[2], livro[3], livro[4])

    html_content += """
    </table>
    </body>
    </html>
    """

    with open(caminho_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Relatório HTML gerado com sucesso em: {caminho_html}")
