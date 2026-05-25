class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):

        if len(self.data) == 0:
            return None

        return self.data.pop()

    def kosong(self):
        return len(self.data) == 0