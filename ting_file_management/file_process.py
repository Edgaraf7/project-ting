import os
from queue import Queue
from file_management import txt_importer


def process(queue, file_path):
    # Verificar se o arquivo já foi processado anteriormente
    file_name = os.path.basename(file_path)
    if file_name in queue.processed_files:
        return

    # Ler as linhas do arquivo usando txt_importer
    lines = txt_importer(file_path)

    # Verificar se as linhas foram lidas com sucesso
    if lines is None:
        return

    # Construir o dicionário com os dados processados
    processed_data = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    # Adicionar o arquivo à fila
    queue.enqueue(processed_data)

    # Mostrar os dados processados via stdout
    print(processed_data)


if __name__ == "__main__":
    queue = Queue()  # Crie uma instância da fila
    file_path = "exemplo.txt"  # Caminho do arquivo
    process(queue, file_path)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
