class Queue:
    def __init__(self):
        self.data = []

    def enque(self, item):
        self.data.append(item)

    def deque(self):

        if len(self.data) == 0:
            return None

        return self.data.pop(0)