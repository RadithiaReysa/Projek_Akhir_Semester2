class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):

        if len(self.data) == 0:
            return None

        return self.data.pop(0)