from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    conn = psycopg2.connect(
        host="localhost",
        database="data",
        user="postgres",
        password="bukitbaling19"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        alamat = request.form.get("alamat")
        delegasi = request.form.get("delegasi")
        telepon = request.form.get("telepon")
        query = f"insert into data(nama, alamat, delegasi, telepon) values('{nama}', '{alamat}', '{delegasi}', '{telepon}')"
        curs.execute(query)
        conn.commit()
    
        # print(20*"=")
        # print(request.form)
        # print(request.form.get("nama"))
        # print(request.form.get("detail"))
        # print(20*"=")
    
    print(request.method)
    query = f"select * from data order by id desc"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()

    
    return render_template("index.html", context=data)

if __name__ == "__main__":
    app.run()