class Stack:
    def __init__(self):
        self.store = []

    @property
    def size(self):
        return len(self.store)

    @property
    def is_empty(self):
        return len(self.store) == 0

    def push(self, v):
        self.store.append(v)

    def pop(self):
        return self.store.pop()
