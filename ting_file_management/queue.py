from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def search(self, index):
        if not 0 <= index < len(self.items):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.items[index]

    def is_empty(self):
        return len(self.items) == 0
