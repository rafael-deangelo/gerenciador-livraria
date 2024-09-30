import shutil
from datetime import datetime
import os

def criar_estrutura_diretorios():
    # Estrutura de diretórios
    diretorios = ['backups', 'data', 'exports']
    for dir_name in diretorios:
        # Cria o diretório se não existir
        os.makedirs(dir_name, exist_ok=True)
    print('Estrutura de diretórios verificada/criada.')


def criar_backup():
    # Diretório de backups
    diretorio_backup = 'backups'
    os.makedirs(diretorio_backup, exist_ok=True)

    # Nome do arquivo de backup com data e hora
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    caminho_backup = os.path.join(diretorio_backup, f'backup_livraria_{timestamp}.db')

    # Copiar o arquivo do banco de dados para o diretório de backup
    shutil.copy('data/livraria.db', caminho_backup)

    print(f'Backup criado com sucesso: {caminho_backup}')


def limpar_backups_antigos():
    caminho_backup = 'backups'
    arquivos_backup = sorted(os.listdir(caminho_backup), key=lambda x: os.path.getmtime(os.path.join(caminho_backup, x)), reverse=True)

    # Manter apenas os 5 backups mais recentes
    print(f'Aguarde...Esse processo pode demorar!')
    if len(arquivos_backup) > 5:
        for arquivo_antigo in arquivos_backup[5:]:
            os.remove(os.path.join(caminho_backup, arquivo_antigo))  # Remove o arquivo
            print(f'Removendo backup antigo: {arquivo_antigo}')
    else:
        print('Nenhum backup antigo a ser removido.')

# Chame a função para criar a estrutura de diretórios ao iniciar o programa
criar_estrutura_diretorios()
