class Storage:
    def export_hasil(self, data):
        with open("hasil_voting.txt", "w") as file:
            file.write("HASIL VOTING\n\n")

            for kandidat in data:
                file.write(
                    f"{kandidat.nama} : {kandidat.suara} suara\n"
                )
        print("Berhasil export")