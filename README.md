# LIBRARY MANAGEMENT SYSTEM (PYTHON BASED)
User: mega-Chlh\
Batch 9 Business Intelligence / Data Analyst @ Pacmann

## Tujuan pengerjaan projek
Projek ini bertujuan untuk membuat Library Management System (LMS) sederhana dengan menggunakan bahasa pemrograman Python,
dan mengoneksikan LMS tersebut dengan database di MySQL Workbench.

## Deskripsi

***Mengoneksikan python dengan mysql, mengembalikan variabel koneksi***\
`create_server_cnx(host_name, user_name, user_password)`

***Membuat database pada mysql***\
`create_db(connection, query)`

***Mengeksekusi query pada mysql***\
Fungsi ini akan mengeksekusi seluruh query yang didefinisikan pada modul `create_db_table`.\
Fungsi ini akan membuat tiga tabel utama, yaitu: **buku**, **anggota** dan **peminjaman**.\
`execute_query(connection, query)`

***Mendaftarkan user baru, mengupdate tabel anggota***\
Fungsi ini akan mengizinkan user untuk menginput prompt yang berisi data anggota baru.\
Setelah menerima input, fungsi ini akan mengupdate tabel anggota pada database mysql.\
`registeruser()`

***Mendaftarkan buku baru, mengupdate tabel buku***\
Fungsi ini akan mengizinkan user untuk menginput prompt yang berisi data buku baru.\
Setelah menerima input, fungsi ini akan mengupdate tabel buku pada database mysql.\
`registerbuku()`

***Meminjam buku, mengupdate stok buku dan tabel peminjaman***\
Fungsi ini akan mengizinkan user untuk menginput prompt yang berisi data buku yang akan dipinjam.\
Berdasarkan input, fungsi ini akan mengupdate tabel peminjaman pada database mysql.\
Fungsi ini juga akan mengupdate stok buku yang terdapat pada tabel buku.\
 `pinjambuku()`
 
 ***Menampilkan daftar buku di perpustakaan***\
 Fungsi ini akan menampilkan seluruh data buku yang terdapat di tabel buku pada database mysql.\
 `lihatbuku()`
 
 ***Menampilkan daftar anggota di perpustakaan***\
 Fungsi ini akan menampilkan seluruh data anggota yang terdapat di tabel anggota pada database mysql.\
 `lihatuser()`
 
 ***Menampilkan daftar peminjaman di perpustakaan***\
 Fungsi ini akan menampilkan seluruh data peminjaman yang terdapat di tabel peminjaman pada database mysql.\
 `lihatpinjam()`
 
 ***Mencari buku berdasarkan judul buku***\
 Fungsi ini akan melakukan pencarian buku berdasarkan parameter judul buku pada tabel buku.\
 Fungsi ini akan mengembalikan seluruh hasil yang memiliki kesamaan kata berdasarkan input user.\
 `caribuku()`
 
 ***Mengembalikan buku yang sudah dipinjam, menghapus data dari daftar 
 peminjaman dan mengupdate stok buku***\
 Fungsi ini akan menghapus data peminjaman pada tabel peminjaman di database mysql.\
 Fungsi ini juga akan mengupdate stok buku pada tabel buku di database mysql.\
 `kembalikan()`
 

## Cara Penggunaan Program
1. Download modul 'mega-Chlh-python-4.py' dan 'create_table_db.py', simpan dalam satu folder yang sama
2. Pastikan anda sudah menginstall  mysqlconnector & pandas pada terminal anda
3. Eksekusi modul 'mega-Chlh-python-4.py' pada IDE pilihan anda

## Hasil Test Case

1. Registrasi anggota baru
<img width="578" alt="image" src="https://user-images.githubusercontent.com/109532941/182408839-8f4292f0-eda5-40d8-a13d-79edf5f111c8.png">

2. Menampilkan data anggota setelah registrasi
<img width="476" alt="image" src="https://user-images.githubusercontent.com/109532941/182409352-7ce43134-c755-4877-b44a-9b425aa32933.png">

3. Registrasi buku baru
<img width="334" alt="image" src="https://user-images.githubusercontent.com/109532941/182410141-4777f1d1-75d3-4767-8cab-8ddfbb888dec.png">

4. Menampilkan data buku
<img width="349" alt="image" src="https://user-images.githubusercontent.com/109532941/182410491-53f9e3de-5a4e-4d4c-b02d-716e57273aa7.png">

5. Melakukan peminjaman
<img width="338" alt="image" src="https://user-images.githubusercontent.com/109532941/182410768-a855d57a-d724-459c-8518-79d72bc4d68c.png">

6. Menampilkan data peminjaman
<img width="485" alt="image" src="https://user-images.githubusercontent.com/109532941/182410912-20169cb3-fc8b-4c60-8433-48875a68fa31.png">

7. Menampilkan data buku setelah peminjaman (stok berkurang)
<img width="358" alt="image" src="https://user-images.githubusercontent.com/109532941/182411308-10a7afb6-7007-4141-b9f9-a49a2a3a2583.png">

8. Mengembalikan buku
<img width="341" alt="image" src="https://user-images.githubusercontent.com/109532941/182411706-833ad9f4-8023-44da-8d2e-144ba0f4edea.png">

9. Menampilkan data peminjaman setelah pengembalian (data di peminjaman terhapus)
<img width="335" alt="image" src="https://user-images.githubusercontent.com/109532941/182411970-b1482a24-360d-48c6-9546-6ee5c13254c8.png">

10. Menampilkan data buku setelah peminjaman (stok bertambah kembali)
<img width="353" alt="image" src="https://user-images.githubusercontent.com/109532941/182412355-7d31388e-3ddb-4bfc-a76b-30cb781ccf44.png">



