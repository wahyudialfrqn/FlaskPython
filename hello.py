from flask import Flask, request, redirect, url_for, render_template
import os
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def hello_world():
     return render_template('main.html')

@app.route('/fakultas')
def fakultas():
    fakultas = ["FIKR", "FEB"]
    return render_template('fakultas.html', fakultas=fakultas)

@app.route('/prodi')
def prodi():
    prodi = [
        {"nama": "Informatika", "fakultas": "FIKR"},
        {"nama": "Sistem Informasi", "fakultas": "FIKR"},
        {"nama": "Akuntansi", "fakultas": "FEB"}
    ]
    return render_template('prodi.html', prodi=prodi)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']
        print(f"Nama: {name}, Email : {email}, Pesan: {pesan}")
        pesan_konfirmasi = f"Halo {name}, data Anda Berhasil dikirim"
      
        return render_template ('contact.html', nama=name, email=email, pesan=pesan, pesan_konfirmasi=pesan_konfirmasi)
    return render_template('contact.html')

@app.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        nisn = request.form['nisn']
        nama = request.form['nama']
        email = request.form['email']
        tanggalLahir = request.form['tanggalLahir']
        asalSekolah = request.form['asalSekolah']
        prodi = request.form['prodi']
        print(f"NISN: {nisn}, Nama: {nama}, Email: {email}, Tanggal Lahir: {tanggalLahir}, Asal Sekolah: {asalSekolah}, Prodi: {prodi}")
        foto = request.files['foto']
        if foto:
            # Mengambil timestamp saat ini untuk menambahkan ke nama file
            timestamp = str(int(time.time()))
          # Mengambil ekstensi file asli
            ext = foto.filename.split('.')[-1]

            # Menambahkan ekstensi ke nama file unik
            unique_filename = f"{timestamp}.{ext}"

            # Menyimpan file dengan nama unik
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            foto.save(foto_path)
            foto_path = f'uploads/{unique_filename}'  # Menyimpan path relatif dengan menggunakan '/uploads/'
            foto_url = f'/static/uploads/{unique_filename}'
        else:
            foto_path = None
        pesan_konfirmasi = f"Terimakasih {nama}, anda telah mendaftarkan diri di Universitas MDP"
      
        return render_template ('registrasi.html', nisn=nisn, nama=nama, email=email, tanggalLahir=tanggalLahir, asalSekolahir=asalSekolah, prodi=prodi, pesan_konfirmasi=pesan_konfirmasi, foto=foto_path)
    return render_template('registrasi.html')

if __name__ == '__main__':
    app.run(debug=True)