import sys
from typing import Union
from ting_file_management.queue import Queue


def process(file_path: str, project: Queue) -> None:
    # Verificar se o arquivo já foi processado anteriormente
    for item in project.items:
        if item["nome_do_arquivo"] == file_path:
            print(f"Arquivo {file_path} já processado anteriormente. Ignorando.")
            return

    # Definição da função txt_importer localmente
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

    # Importar o conteúdo do arquivo usando a função txt_importer local
    lines = txt_importer(file_path)

    # Se o conteúdo do arquivo for None, significa que houve um erro na importação
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

def remove(project: Queue) -> None:
    if len(project) == 0:
        print("Não há elementos")
        return

    removed_file = project.dequeue()
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(project: Queue, index: int) -> None:
    try:
        file_info = project.search(index)
        print("Informações do arquivo:")
        print(file_info)
    except IndexError:
        sys.stderr.write("Posição inválida\n")
