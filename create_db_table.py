import mysql.connector 
from mysql.connector import Error

# Fungsi membuat koneksi ke MySQL

def create_server_cnx(host_name, user_name, user_password):
    mydb = None
    try:
        mydb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: {err}")
    return mydb

# Fungsi membuat database

def create_db(connection, query):
    mycursor = connection.cursor()
    try:
        mycursor.execute(query)
        print("Database successfully created")
    except Error as err:
        print(f"Error: {err}")

# Fungsi execute query

def execute_query(connection, query):
    mycursor = connection.cursor()
    try:
        mycursor.execute(query)
        mydb.commit()
    except Error as err:
        print(f"Error: {err}")              

# Definisi initial query

q_create_db = '''CREATE DATABASE lms_python;'''
              
q_use_db = '''USE lms_python;'''

q_table_buku = '''CREATE TABLE buku(
                        id_buku INT NOT NULL AUTO_INCREMENT,
                        judul_buku VARCHAR(50),
                        kategori VARCHAR(50),
                        stok INT,
                        PRIMARY KEY (id_buku)
                    );
                '''

q_table_anggota = '''CREATE TABLE anggota(
                            id_anggota INT NOT NULL AUTO_INCREMENT,
                            u_anggota VARCHAR(50) UNIQUE,
                            tgl_lahir DATE,
                            profesi VARCHAR(50),
                            domisili VARCHAR(50),
                            PRIMARY KEY (id_anggota)
                        );
                    '''


q_table_peminjaman = '''CREATE TABLE peminjaman(
                                id_anggota INT,
                                u_anggota VARCHAR(50),
                                id_buku INT,
                                judul_buku VARCHAR(50),
                                tgl_pinjam DATE DEFAULT (CURDATE()),
                                tgl_kembali DATE DEFAULT (CURDATE() + INTERVAL 7 DAY),
                                FOREIGN KEY (id_anggota) REFERENCES anggota(id_anggota),
                                FOREIGN KEY (id_buku) REFERENCES buku(id_buku)
                        );
                    '''

q_insert_buku = '''INSERT INTO buku
                    VALUES(1, 'Aroma Karsa', 'Novel', 8),
                    (2, 'Madre', 'Novel', 8),
                    (3, 'Python for Dummies', 'Data', 7),
                    (4, 'SQL for Dummies', 'Data', 6),
                    (5, 'Si Kancil', 'Buku Anak', 5);
                '''

q_insert_anggota = '''INSERT INTO anggota
                        VALUES(1000, 'Ade_P', '1955-04-02', 'Pensiunan', 'Bandung'),
                        (1001, 'Budi_W', '1988-02-09', 'PNS', 'Surabaya'),
                        (1002, 'Abdul_H', '1990-10-10', 'PNS', 'Surabaya'),
                        (1003, 'Rosie_B', '1996-06-02', 'Mahasiswa', 'Jogja'),
                        (1004, 'Rita_S', '1982-01-01', 'Ibu Rumah Tangga', 'Jogja');
                    '''

# Mengeksekusi pembuatan database
# Masukkan nama host, nama user, dan password sesuai komputer anda

mydb = create_server_cnx('localhost', 'root', 'Jakarta171096')

# Menjalankan fungsi create database dan use database

create_db(mydb, q_create_db)
execute_query(mydb, q_use_db)
