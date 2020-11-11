class Queue():
    """
    Итератор, для реализации очереди
    """
    def __init__(self, collection=[]):
        self.collection = collection
        self.cursor = 0

    def current(self):
        if self.cursor < len(self.collection):
            return self.collection[self.cursor]

    def next(self):
        if len(self.collection) >= self.cursor + 1:
            self.cursor += 1

    def has_next(self):
        has = len(self.collection) >= self.cursor + 1
        if not has: self.cursor = 0
        return has

    def add(self, item):
        self.collection.append(item)

    def pop(self, item):
        return self.collection.pop(item)


class Visited():
    """
    Итератор, для отметки посещенных станций
    """
    def __init__(self, collection=set()):
        self.collection = collection

    def list(self):
        return list(self.collection)

    def has(self, item):
        return item in self.collection

    def add(self, item):
        self.collection.add(item)

    def remove(self, item):
        self.collection.remove(item)