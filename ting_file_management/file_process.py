import os
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    # Verificar se o arquivo já foi processado anteriormente
    file_name = os.path.basename(path_file)
    if instance.is_processed(file_name):
        print(f"Arquivo {file_name} já foi processado anteriormente")
        return

    # Ler as linhas do arquivo usando txt_importer
    lines = txt_importer(path_file)

    # Verificar se as linhas foram lidas com sucesso
    if lines is None:
        return

    # Construir o dicionário com os dados processados
    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    # Adicionar o arquivo à fila
    instance.enqueue(processed_data)

    # Mostrar os dados processados via stdout
    print(processed_data)


def remove(instance: Queue):
    try:
        file_info = instance.dequeue()
        print(f"Arquivo {file_info['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos para remover")
    except TypeError:
        print("Não há elementos para remover")


def file_metadata(instance: Queue, position):
    try:
        file_info = instance.search(position)
        print(file_info)
    except IndexError:
        print("Posição inválida")
