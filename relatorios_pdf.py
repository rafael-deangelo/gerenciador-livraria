from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def gerar_relatorio_pdf(livros, caminho_pdf):
    # Criação do canvas (documento PDF)
    c = canvas.Canvas(caminho_pdf, pagesize=A4)

    # Definir a largura e altura da página
    width, height = A4

    # Título do Relatório em negrito
    c.setFont("Helvetica-Bold", 12)  # Define fonte em negrito
    c.drawString(100, height - 50, "Relatório de Livros")

    # Definir a posição inicial para imprimir os dados
    y_position = height - 100

    # Iterar sobre os livros e imprimir no PDF
    for livro in livros:
        # Exibir o título, autor e ano em uma linha em negrito
        c.setFont("Helvetica-Bold", 10)  # Fonte em negrito para os labels
        c.drawString(100, y_position, f"ID:")
        c.drawString(150, y_position, f"{livro[0]}")
        c.drawString(200, y_position, "Título:")
        c.drawString(250, y_position, f"{livro[1]}")
        y_position -= 20  # Move a posição da linha para baixo

        c.setFont("Helvetica-Bold", 10)  # Fonte em negrito para os labels
        c.drawString(100, y_position, "Autor:")
        c.setFont("Helvetica", 10)  # Fonte normal para o valor
        c.drawString(150, y_position, f"{livro[2]}")

        c.setFont("Helvetica-Bold", 10)  # Fonte em negrito para os labels
        c.drawString(300, y_position, "Ano:")
        c.setFont("Helvetica", 10)  # Fonte normal para o valor
        c.drawString(350, y_position, f"{livro[3]}")

        c.setFont("Helvetica-Bold", 10)  # Fonte em negrito para os labels
        c.drawString(400, y_position, "Preço:")
        c.setFont("Helvetica", 10)  # Fonte normal para o valor
        c.drawString(450, y_position, f"R$ {livro[4]:.2f}")

        y_position -= 40  # Move mais a posição para a próxima entrada de livro

        # Se atingir o fim da página, cria uma nova página
        if y_position < 50:
            c.showPage()  # Adiciona uma nova página
            y_position = height - 100  # Reinicia a posição na nova página

    # Finaliza o documento e salva
    c.save()

    print(f"Relatório PDF gerado com sucesso em: {caminho_pdf}")
