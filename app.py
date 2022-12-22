from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/berita')
def berita():
    return render_template('berita.html')

@app.route('/berita/berita1')
def berita1():
    return render_template('berita1.html')

@app.route('/berita/berita2')
def berita2():
    return render_template('berita2.html')        

@app.route('/berita/berita3')
def berita3():
    return render_template('berita3.html')

@app.route('/berita/berita4')
def berita4():
    return render_template('berita4.html')

@app.route('/aduanmasyarakat')
def aduanmasyarakat():
    return render_template('aduanmasyarakat.html')

@app.route('/aduanmasyarakat/sukses')
def aduanmasyarakatsuccess():
    return render_template('aduanmasyarakatsuccess.html')      

@app.route('/profildki/sejarah')
def sejarahdki():
    return render_template('sejarahdki.html')

@app.route('/profildki/visimisi')
def visimisidki():
    return render_template('visimisidki.html')

@app.route('/profildki/pimpinan')
def pimpinandki():
    return render_template('pimpinandki.html') 

@app.route('/profildki/kantor')
def alamatdki():
    return render_template('alamatdki.html')  

if __name__ == '__main__':
    app.run(debug=True)