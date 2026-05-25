from models import Kandidat
from single_linked_list import SingleLinkedList
from Circular_Linked_List import CircularLinkedList
from doubly_linked_list import DoublyLinkedList

class Pemilihan:
    def __init__(self):
        self.kandidat = SingleLinkedList()
        self.pemilih = {}
        self.slide_show = CircularLinkedList()
        self.navigasi = DoublyLinkedList()

    #pilih 1
    def registrasi(self,nim,nama):
        if nim in self.pemilih:
            return
        
        self.pemilih[nim] = nama

    #pilih 2
    def tambah_kandidat(self, nomor, nama, vm):

        calon = Kandidat(
            nomor,
            nama,
            vm
        )
       
        self.kandidat.tambah_belakang(calon)
        
        self.navigasi.tambah(calon)
        
        self.slide_show.tambah(calon)

    #pilih 3
    def hapus_kandidat(self,nomor):
        pass
    
    #pilih 4
    def undo(self):
        pass
    
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
        pass

    #pilih 8
    def panggil(self):
        pass

    #pilih 9
    def voting(self, nim, nomor, dukung=None):
        pass
    
    #pilih 10
    def hasil(self):
        pass
    
    #pilih 11
    def cari_pemilih(self, nim):
        if nim in self.pemilih:
            print(nim, "-", self.pemilih[nim])

    #pilih 12
    def tampil_graph(self):
        pass
    
    #pilih 13
    def export(self):

        pass
    
    #pilih 14
    def slide(self):
        self.slide_show.slide()
    
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