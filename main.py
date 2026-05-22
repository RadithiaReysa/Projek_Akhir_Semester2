from pemilihan import Pemilihan

def menu():
    sistem = Pemilihan()

    while True:
        print("\n==============================")
        print(" SIMULATOR PEMILIHAN KETUA")
        print("==============================")
        print("1. Registrasi pemilih")
        print("2. Tambah kandidat")
        print("3. Hapus kandidat")
        print("4. Undo aksi admin")
        print("5. Lihat kandidat")
        print("6. Detail kandidat")
        print("7. Antre pemilih")
        print("8. Panggil pemilih berikutnya")
        print("9. Voting")
        print("10. Hasil voting")
        print("11. Cari pemilih")
        print("12. Tampilkan graph dukungan")
        print("13. Ekspor hasil")
        print("0. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            nim = input("NIM : ")
            nama = input("Nama : ")
            sistem.registrasi(nim, nama)

        elif pilihan == "2":
            nomor = int(input("Nomor : "))
            nama = input("Nama : ")
            vm = input("Visi Misi : ")
            sistem.tambah_kandidat(nomor, nama, vm)

        elif pilihan == "3":
            nomor = int(input("Nomor : "))
            sistem.hapus_kandidat(nomor)

        elif pilihan == "4":
            sistem.undo()

        elif pilihan == "5":
            sistem.lihat_kandidat()

        elif pilihan == "6":
            nomor = int(input("Nomor : "))
            sistem.detail_kandidat(nomor)

        elif pilihan == "7":
            nim = input("NIM : ")
            sistem.antre(nim)

        elif pilihan == "8":
            sistem.panggil()

        elif pilihan == "9":
            nim = input("NIM : ")
            nomor = int(input("Nomor kandidat : "))
            dukung = input("Dukung siapa (opsional): ")
            if dukung == "":
                dukung = None
            sistem.voting(nim, nomor, dukung)

        elif pilihan == "10":
            sistem.hasil()

        elif pilihan == "11":
            nim = input("NIM : ")
            sistem.cari_pemilih(nim)

        elif pilihan == "12":
            sistem.tampil_graph()

        elif pilihan == "13":
            sistem.export()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    menu()

# test