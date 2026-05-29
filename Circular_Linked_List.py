class CircularNode:

    def __init__(self, data):

        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):

        self.head = None

    def tambah(self, data):

        node_baru = CircularNode(data)

        if self.head is None:

            self.head = node_baru
            node_baru.next = self.head
            return

        current = self.head

        while current.next != self.head:

            current = current.next

        current.next = node_baru
        node_baru.next = self.head

    def tampil_slide(self):

        if self.head is None:

            print("Data kosong")
            return

        current = self.head

        while True:

            print(current.data.tampil_ringkas())

            lanjut = input("Next slide? (y/n) : ")

            if lanjut == "n":
                break

            current = current.next