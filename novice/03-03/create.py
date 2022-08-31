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
nama = "kyubi"
umur = 24
query = f"insert into siswa(nama, umur) values('{nama}', {umur})"

curs.execute(query)
conn.commit()
