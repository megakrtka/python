import mysql.connector
from mysql.connector import Error
import pandas as pd

# Mengimpor fungsi pembuatan database

from create_db_table import *

# Mengeksekusi fungsi input data dari modul create table

try:
    execute_query(mydb, q_table_buku)
    execute_query(mydb, q_table_anggota)
    execute_query(mydb, q_table_peminjaman)
    execute_query(mydb, q_insert_buku)
    execute_query(mydb, q_insert_anggota)
    print("Database successfully connected")
except:
    print("Database connection was not successful")

# Membuat kursor yang mengoneksikan dengan database
# Masukkan nama host, nama user dan password sesuai komputer anda
# Nama database tidak perlu diganti

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jakarta171096",
        database="lms_python"
        )
mycursor = mydb.cursor()    

# Fungsi menambahkan user baru, mengupdate tabel anggota

def registeruser():
    u_name = input("Masukkan username baru: ")
    ttl = input("Masukkan tanggal lahir anda (YYY-MM-DD): ")
    pekerjaan = input("Masukkan pekerjaan anda: ")
    lokasi = input("Masukkan domisili anda: ")
    data_user = (u_name, ttl, pekerjaan, lokasi)
    query_register_user = '''INSERT INTO anggota(u_anggota, tgl_lahir, profesi, domisili) 
                VALUES(%s, %s, %s, %s);'''
    try:
        mycursor.execute(query_register_user, data_user)
        mydb.commit()
        print("Registrasi user baru berhasil!")
    except Error as err:
        print(f"Error: {err}")
        
# Fungsi menambahkan buku baru, mengupdate tabel buku  

def registerbuku():
    judul = input("Masukkan judul buku: ")
    kat_buku = input("Masukkan kategori buku: ")
    stok_buku = int(input("Masukkan stok: "))
    data_buku = (judul, kat_buku, stok_buku)
    query_register_buku = '''INSERT INTO buku(judul_buku, kategori, stok) VALUES(%s, %s, %s);'''
    try:
        mycursor.execute(query_register_buku, data_buku)
        mydb.commit()
        print("Registrasi buku baru berhasil!")
    except Error as err:
        print(f"Error: {err}")
        
# Fungsi meminjam buku, mengupdate stok buku dan tabel peminjaman

def pinjambuku():
    id_user = int(input("Masukkan id anda: "))
    user_pinjam = input("Masukkan username anda: ")
    id_buku = int(input("Masukkan id buku: "))
    judul_buku = input("Masukkan judul buku: ")
    data_pinjam_user_buku = (id_user, user_pinjam, id_buku, judul_buku)
    data_pinjam_buku = (id_buku,)
    query_update_stok_pinjam = '''UPDATE buku SET stok = (stok - 1) WHERE id_buku= %s ;'''
    query_data_pinjam = '''INSERT INTO peminjaman(id_anggota, u_anggota, id_buku, judul_buku) VALUES(%s, %s, %s, %s);'''
    try:
        mycursor.execute(query_update_stok_pinjam, data_pinjam_buku)
        mycursor.execute(query_data_pinjam, data_pinjam_user_buku)
        mydb.commit()
        print(f"Buku berhasil dipinjam oleh: {user_pinjam}")
    except Error as err:
        print(f"Error: {err}")

# Fungsi menampilkan daftar buku di perpustakaan
        
def lihatbuku():
    query_lihat_buku = '''SELECT * FROM buku;'''
    try:
        mycursor.execute(query_lihat_buku)
        records = mycursor.fetchall()
        df = pd.DataFrame(records)
        df.columns = [description[0] for description in mycursor.description]
        print(df)
    except Error as err:
        print(f"Error: {err}")

# Fungsi menampilkan daftar anggota di perpustakaan
        
def lihatuser():
    query_lihat_user = '''SELECT * FROM anggota;'''
    try:
        mycursor.execute(query_lihat_user)
        records = mycursor.fetchall()
        df = pd.DataFrame(records)
        df.columns = [description[0] for description in mycursor.description]
        print(df)
    except Error as err:
        print(f"Error: {err}")

# Fungsi menampilkan daftar peminjaman di perpustakaan
        
def lihatpinjam():
    query_lihat_pinjam = '''SELECT * FROM peminjaman;'''
    try:
        mycursor.execute(query_lihat_pinjam)
        records = mycursor.fetchall()
        df = pd.DataFrame(records)
        if df.empty:
            print("Tidak ada peminjaman yang berlangsung!")
        else:
            df.columns = [description[0] for description in mycursor.description]
            print(df)
    except Error as err:
        print(f"Error: {err}")

# Fungsi mencari buku berdasarkan judul buku di perpustakaan
        
def caribuku():
    judul = input("Masukkan judul buku: ")
    j_buku = (judul,)
    query_cari_buku = '''SELECT * FROM buku WHERE judul_buku LIKE CONCAT ('%', %s, '%');'''
    try:
        mycursor.execute(query_cari_buku, j_buku)
        records = mycursor.fetchall()
        df = pd.DataFrame(records)
        if df.empty:
            print("Buku yang anda cari tidak tersedia!")
        else:
            df.columns = [description[0] for description in mycursor.description]
            print(df)
    except Error as err:
        print(f"Error: {err}")

# Fungsi mengembalikan buku yang sudah dipinjam, menghapus data dari daftar peminjaman dan mengupdate stok buku     
        
def kembalikan():
    id_pinjam = input("Masukkan id anda: ")
    nama = input("Masukkan username anda: ")
    id_buku = input("Masukkan id buku: ")
    judul = input("Masukkan judul buku: ")
    data_buku = (id_buku,)
    query_kembali = '''DELETE FROM peminjaman WHERE id_buku = %s;'''
    query_update_kembali = '''UPDATE buku SET stok = (stok+1) WHERE id_buku = %s;'''
    try:
        mycursor.execute(query_kembali, data_buku)
        mycursor.execute(query_update_kembali, data_buku)
        mydb.commit()
        print("Buku berhasil dikembalikan!")
    except Error as err:
        print(f"Error: {err}")

# Fungsi menampilkan menu utama dan mengarahkan ke fungsi
        
while True:
    print('''+++LIBRARY MANAGEMENT SYSTEM+++
---------------------------------------------
    1. Register User
    2. Register Buku
    3. Peminjaman Buku
    4. Tampilkan Daftar Buku
    5. Tampilkan Daftar User
    6. Tampilkan Daftar Pinjam
    7. Cari Buku
    8. Pengembalian Buku
    9. Exit
---------------------------------------------
    ''')
    choice = int(input("Masukkan pilihan anda:"))
    if choice == 1:
        registeruser()
    elif choice == 2:
        registerbuku()
    elif choice == 3:
        pinjambuku()
    elif choice == 4:
        lihatbuku()
    elif choice == 5:
        lihatuser()
    elif choice == 6:
        lihatpinjam()
    elif choice == 7:
        caribuku()
    elif choice == 8:
        kembalikan()
    else:
        print("Sampai jumpa lagi!")
        break