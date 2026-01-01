from flask import Flask, render_template, request

app = Flask(__name__)

# Menggunakan rute /login sesuai instruksi form login
@app.route("/login", methods=["GET", "POST"])
def login():
    hasil = ""
    if request.method == "POST":
        # Mengambil data dari input 'nama' di HTML
        nama = request.form.get("nama")
        if nama:
            hasil = f"Halo, {nama}! Login berhasil menggunakan Flask Python."
        else:
            hasil = "Nama tidak boleh kosong!"
            
    # Pastikan memanggil "index.html" karena itu nama file di folder templates kamu
    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
