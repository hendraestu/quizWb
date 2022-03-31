from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route("/hitung", methods=["POST"])
def hitung():
    berat = float(request.form['berat'])
    tinggi = float(request.form['tinggi'])

    bmi = berat / (tinggi/100)**2

    if bmi < 18.5 :
        ket = 'kurus'
    elif bmi > 18.5 and bmi < 25:
        ket = 'normal'
    elif bmi > 25 and bmi < 40:
        ket = 'berlebih'
    else:
        ket = 'bahaya'

    hasil = {'hasil bmi': bmi, 'keterangan': ket}
    return jsonify(hasil)

if __name__ == '__main__':
   app.run(debug = True, port=7092)
