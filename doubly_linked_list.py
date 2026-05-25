class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.current = None

    def tambah(self, data):

        node_baru = DoubleNode(data)

        if self.head is None:

            self.head = node_baru
            self.current = node_baru
            return

        temp = self.head

        while temp.next:

            temp = temp.next

        temp.next = node_baru
        node_baru.prev = temp

    def next_kandidat(self):
        if self.current is None:
            return None

        if self.current.next:
            self.current = self.current.next

        return self.current.data

    def prev_kandidat(self):
        if self.current is None:
            return None

        if self.current.prev:
            self.current = self.current.prev

        return self.current.data