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
query = f"select * from siswa where umur=30"
curs.execute(query)
data = curs.fetchone()
print("nama:", data[0], "umur:", data[1])