from models import Kandidat
from single_linked_list import SingleLinkedList
from Circular_Linked_List import CircularLinkedList
from doubly_linked_list import DoublyLinkedList
from binary_search_tree import BinarySearchTree
from rekursif import Rekursif
from queue import Queue
from storage import Storage
from sorting import bubble_sort
from hash_table import HashTable
from graph import Graph
from stack import Stack

class Pemilihan:
    def __init__(self):
        self.kandidat = SingleLinkedList()
        self.navigasi = DoublyLinkedList()
        self.circular = CircularLinkedList()
        self.queue = Queue()
        self.stack = Stack()
        self.pemilih = HashTable()
        self.graph = Graph()
        self.bst = BinarySearchTree()
        self.rekursif = Rekursif()
        self.storage = Storage()
        self.sudah_voting = set()
        self.rekap_suara = {}

    #pilih 1
    def registrasi(self,nim,nama):
        self.pemilih.tambah(
            nim,
            nama
        )
        self.bst.root = self.bst.insert(
            self.bst.root,
            nim,
            nama
        )
        print("Pemilih berhasil didaftarkan")

    #pilih 2
    def tambah_kandidat(self, nomor, nama, vm):
        calon = Kandidat(
            nomor,
            nama,
            vm
        )
       
        self.kandidat.tambah_belakang(calon)
        self.navigasi.tambah(calon)
        self.circular.tambah(calon)
        self.stack.push(
            ("tambah", calon)
        )

        print("Kandidat berhasil ditambahkan")

    #pilih 3
    def hapus_kandidat(self,nomor):
        kandidat = self.kandidat.hapus_kandidat(nomor)
        if kandidat:
            self.stack.push(
                ("hapus", kandidat)
            )
            print("Kandidat berhasil dihapus")

        else:
            print("Kandidat tidak ditemukan")

    
    #pilih 4
    def undo(self):
        if self.stack.kosong():

            print("Tidak ada undo")
            return
        aksi, kandidat = self.stack.pop()

        if aksi == "hapus":
            self.kandidat.tambah_belakang(kandidat)

        elif aksi == "tambah":
            self.kandidat.hapus_kandidat(
                kandidat.nomor
            )
        print("Undo berhasil")
    
    #pilih 5
    def lihat_kandidat(self):
        self.kandidat.tampilkan_data()
    
    #pilih 6
    def detail_kandidat(self, nomor):
        kandidat = self.kandidat.cari_nomor_kandidat(nomor)

        if kandidat:
            print(kandidat.tampil_ringkas())

        else:
            print("Kandidat tidak ditemukan")
    
    #pilih 7
    def antre(self, nim):
        self.queue.enque(nim)
        print("Masuk Antrean")

    #pilih 8
    def panggil(self):
        data = self.queue.deque()

        if data:
            print("Dipanggil :", data)

        else:
            print("Antrean kosong")


    #pilih 9
    def voting(self, nim, nomor, dukung=None):
        if nim in self.sudah_voting:
            print("Sudah voting")
            return
        
        kandidat = self.kandidat.cari_nomor_kandidat(nomor)

        if kandidat is None:
            print("Kandidat tidak ditemukan")
            return

        kandidat.suara += 1
        self.sudah_voting.add(nim)

        if kandidat.nama not in self.rekap_suara:
            self.rekap_suara[kandidat.nama] = 0

        self.rekap_suara[kandidat.nama] += 1

        if dukung:
            self.graph.tambah_relasi(
                nim,
                dukung
            )
        print("Voting berhasil")
    
    #pilih 10
    def hasil(self):
        data = self.kandidat.to_list()
        data = bubble_sort(data)
        print("\n=== HASIL VOTING ===")

        for kandidat in data:
            print(
                kandidat.nama,
                "-",
                kandidat.suara
            )
    
    #pilih 11
    def cari_pemilih(self, nim):
        hasil = self.pemilih.cari(nim)

        if hasil:
            print(nim, "-", hasil)

        else:
            print("Pemilih tidak ditemukan")

    #pilih 12
    def tampil_graph(self):
        self.graph.tampilkan_graph()
    
    #pilih 13
    def export(self):
        data = self.kandidat.to_list()
        self.storage.export_hasil(data)
    
    #pilih 14
    def slide(self):
        self.circular.tampil_slide()
    
    #pilih 15
    def total_suara_rekursif(self, data):
        if len(data) == 0:
            return 0

        return (
            data[0].suara +
            self.total_suara_rekursif(data[1:])
        )
    
    #pilih 16
    def next_kandidat(self):
        kandidat = self.navigasi.next_kandidat()
        if kandidat:
            print(kandidat.tampil_ringkas())

        else:
            print("Data kandidat kosong")

    #pilih 17
    def prev_kandidat(self):
        kandidat = self.navigasi.prev_kandidat()

        print(kandidat.tampil_ringkas())