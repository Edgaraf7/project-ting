from typing import Union
from ting_file_management.queue import Queue


def txt_importer(file_path: str) -> Union[list, None]:
    import sys

    if not file_path.endswith('.txt'):
        sys.stderr.write("Formato inválido\n")
        return None

    try:
        with open(file_path, 'r') as file:
            lines = file.read().split('\n')
            return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {file_path} não encontrado\n")
        return None


def process(file_path: str, project: Queue) -> None:
    # Verificar se o arquivo já foi processado anteriormente
    if project.search_by_path(file_path):
        print(f"Arquivo {file_path} já processado anteriormente. Ignorando.")
        return

    # Importar o conteúdo do arquivo
    lines = txt_importer(file_path)

    if lines is None:
        return

    # Criar o dicionário com as informações do arquivo
    file_info = {
        "nome_do_arquivo": file_path,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    # Adicionar o dicionário à fila
    project.enqueue(file_info)

    # Exibir os dados processados
    print("Dados processados:")
    print(file_info)
