class HashTable:
    def __init__(self, ukuran=10):
        self.ukuran = ukuran
        self.table = [None] * ukuran

    def hash_function(self, key):
        total = 0
        for huruf in key:
            total += ord(huruf)

        return total % self.ukuran

    def tambah(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []

        for pasangan in self.table[index]:
            if pasangan[0] == key:
                print("NIM sudah terdaftar")
                return

        self.table[index].append(
            (key, value)
        )

    def cari(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        if bucket is None:
            return None
        
        for pasangan in bucket:
            if pasangan[0] == key:
                return pasangan[1]

        return None

    def tampil(self):
        for i in range(self.ukuran):
            print(i, ":", self.table[i])