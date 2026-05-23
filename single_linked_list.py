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