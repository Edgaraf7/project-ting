import sys
from ting_file_management.queue import Queue


def process(file_path: str, project: Queue) -> None:
    if any(item["nome_do_arquivo"] == file_path for item in project.items):
        print(f"Arquivo {file_path} já processado anteriormente.")
        return

    try:
        with open(file_path, 'r') as file:
            lines = file.read().split('\n')
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {file_path} não encontrado\n")
        return

    file_info = {
        "nome_do_arquivo": file_path,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    project.enqueue(file_info)

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
