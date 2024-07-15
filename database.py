# database.py

import mysql.connector
from mysql.connector import errorcode

def create_table():
    try:
        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='perpustakaan'
        )
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS buku (
                id INT AUTO_INCREMENT PRIMARY KEY,
                judul VARCHAR(255),
                penulis VARCHAR(255),
                penerbit VARCHAR(255),
                tahun_terbit INT,
                konten TEXT,
                iktisar TEXT
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ada yang salah dengan username atau password Anda")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database tidak ditemukan")
        else:
            print(err)

def get_buku(judul):
    conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='perpustakaan'
        )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM buku WHERE judul = %s', (judul,))
    buku = cursor.fetchone()
    cursor.close()
    conn.close()
    print(buku) 
    return buku

def post_buku(buku):
    conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='perpustakaan'
        )
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, '\n'.join(buku.konten), buku.iktisar))
    conn.commit()
    cursor.close()
    conn.close()
