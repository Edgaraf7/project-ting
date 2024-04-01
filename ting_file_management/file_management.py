import sys


def txt_importer(file_path):
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


file_path = "exemplo.txt"
lines = txt_importer(file_path)
if lines is not None:
    for line in lines:
        print(line)
