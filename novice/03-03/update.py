try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="bukitbaling19")

except Exception as e:
    print(e)

curs = conn.cursor()
namaLama = "kyubi"

namaBaru = "Kyubong"
umurBaru = 23
query = f"update siswa set nama='{namaBaru}', umur={umurBaru} where nama='{namaLama}'" 

curs.execute(query)
conn.commit()
print("data berhasil diupdate")
