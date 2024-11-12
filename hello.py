from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

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


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)