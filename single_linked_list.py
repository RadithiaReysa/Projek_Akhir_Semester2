from models import Kandidat

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_belakang(self, data):
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node_baru

    def tampilkan_data(self):
        if self.head is None:
            return "Data kandidat kosong"
        
        cur = self.head
        while cur:
            print(cur.data.tampil_ringkas())
            cur = cur.next

    def cari_nomor_kandidat(self,nomor):
        cur = self.head

        while cur:
            if cur.data.nomor == nomor:
                return cur.data
            cur = cur.next

        return None
    
    def hapus_kandidat(self, nomor):

        current = self.head
        previous = None

        while current:

            if current.data.nomor == nomor:

                if previous is None:

                    self.head = current.next

                else:

                    previous.next = current.next

                return current.data

            previous = current
            current = current.next

        return None

    def to_list(self):

        hasil = []
        cur = self.head

        while cur is not None:
            hasil.append(cur.data)
            cur = cur.next

        return hasil