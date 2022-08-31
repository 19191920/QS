try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="bukitbaling19")


    curs = conn.cursor()
    
    nama = "Kyubong"

    query = f"delete from siswa where nama='{nama}'" 
    curs.execute(query)
    conn.commit()
    print("data dihapus")
except Exception as e:
    print(e)    

