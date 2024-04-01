from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.items = []
        self.processed_files = set()

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)
        file_name = value.get("nome_do_arquivo")
        self.processed_files.add(file_name)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def search(self, index):
        if not 0 <= index < len(self.items):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.items[index]

    def is_processed(self, file_name):
        return file_name in self.processed_files
