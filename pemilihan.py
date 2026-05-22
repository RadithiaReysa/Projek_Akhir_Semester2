from models import Kandidat
from single_linked_list import SingleLinkedList

class Pemilihan:
    def __init__(self):
        self.kandidat = SingleLinkedList()
        self.pemilih = {}

    #pilih 1
    def registrasi(self,nim,nama):
        if nim in self.pemilih:
            return
        
        self.pemilih[nim] = nama

    #pilih 2
    def tambah_kandidat(self,nomor,nama,vm):
        calon = Kandidat(nomor,nama,vm)
        self.kandidat.tambah_belakang(calon)

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