class Kandidat:
    def __init__(self, nomor, nama, visi_misi):
        self.nomor = nomor
        self.nama = nama
        self.visi_misi = visi_misi
        self.suara = 0

    def tampil_ringkas(self):
        return f"{self.nomor}. {self.nama} | Suara: {self.suara}"
    