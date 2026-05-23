# Projek_Akhir_Semester2
================================================================
    PROGRAM SIMULATOR PEMILIHAN KETUA ORGANISASI
================================================================


A. MATERI & IMPLEMENTASI
----------------------------------------------------------------

1.  Sorting
    Mengurutkan hasil akhir voting berdasarkan perolehan suara
    terbanyak ke tersedikit untuk ditampilkan di papan hasil.

2.  File Handler
    Menyimpan data kandidat, data pemilih, dan rekap hasil
    voting ke file .txt atau .csv sebagai arsip permanen.

3.  Searching
    Mencari data pemilih berdasarkan nama atau NIM untuk
    memverifikasi apakah pemilih sudah terdaftar dan belum
    memberikan suara.

4.  Rekursif
    Menghitung total suara sah dari seluruh pemilih secara
    rekursif, serta menghitung persentase perolehan suara
    tiap kandidat.

5.  List, Tuple, Set, Dictionary
    - Dictionary : menyimpan {nama_kandidat: jumlah_suara}
    - Set         : menyimpan NIM pemilih yang sudah voting
                    agar tidak dapat dobel
    - Tuple       : menyimpan data kandidat yang tidak boleh
                    diubah (nomor urut, nama)

6.  Stack / Queue
    - Queue : mengatur antrean pemilih
    - Stack : menyimpan riwayat aksi admin (tambah/hapus
              kandidat) agar dapat di-undo

7.  OOP
    - Class Kandidat  : nomor urut, nama, visi-misi, jumlah suara
    - Class Pemilih   : NIM, nama, status voting
    - Class Pemilihan : controller utama seluruh proses

8.  Single Linked List
    Menyimpan daftar seluruh kandidat yang terdaftar
    dalam pemilihan.

9.  Double Linked List
    Navigasi profil kandidat maju/mundur saat pengguna
    ingin melihat detail tiap kandidat.

10. Circular Linked List
    Menampilkan profil kandidat secara berputar terus-menerus
    seperti slideshow pada sesi pengenalan kandidat.

11. Tree
    Digunakan sebagai struktur Binary Search Tree (BST) untuk
    menyimpan dan mencari data pemilih berdasarkan NIM
    secara efisien.

12. Graph
    Merepresentasikan hubungan dukungan antar pemilih
    (siapa mendukung siapa), sehingga dapat dianalisis
    pola dukungan dalam kelompok/kelas.

13. Hash Table
    Menyimpan data pemilih dengan NIM sebagai key untuk
    validasi cepat apakah seseorang sudah terdaftar atau
    sudah memberikan suara.


================================================================

B. FITUR PROGRAM
----------------------------------------------------------------

1.  Registrasi Pemilih
    Admin dapat mendaftarkan pemilih beserta NIM dan namanya
    sebelum sesi voting dimulai. Data disimpan ke file
    dan Hash Table.

2.  Pendaftaran Kandidat
    Admin dapat menambahkan kandidat beserta nomor urut dan
    visi-misinya. Kandidat disimpan dalam Single Linked List.

3.  Tampilan Profil Kandidat (Slideshow)
    Pengguna dapat menelusuri profil semua kandidat satu per
    satu menggunakan Circular Linked List, dapat maju maupun
    mundur dengan Double Linked List.

4.  Proses Voting
    Pemilih memasukkan NIM untuk diverifikasi, lalu memilih
    nomor urut kandidat. Sistem memastikan setiap NIM hanya
    dapat memilih satu kali menggunakan Set dan Hash Table.

5.  Antrean Pemilih
    Pemilih yang datang bersamaan dimasukkan ke dalam Queue
    dan dipanggil satu per satu secara berurutan.

6.  Papan Hasil Real-Time
    Menampilkan perolehan suara semua kandidat beserta
    persentasenya yang diperbarui setiap ada suara masuk,
    diurutkan dengan Sorting.

7.  Analisis Jaringan Dukungan
    Menampilkan visualisasi sederhana (adjacency list)
    hubungan dukungan antar pemilih menggunakan Graph.

8.  Pencarian Data Pemilih
    Admin dapat mencari pemilih berdasarkan nama atau NIM
    menggunakan Searching dan BST Tree untuk hasil lebih cepat.

9.  Undo Aksi Admin
    Admin dapat membatalkan aksi terakhir (misalnya penghapusan
    kandidat yang tidak sengaja) menggunakan Stack.

10. Ekspor Hasil Pemilihan
    Setelah voting ditutup, sistem mengekspor rekap lengkap
    (kandidat, suara, persentase, pemenang) ke file .txt
    menggunakan File Handler.

================================================================
