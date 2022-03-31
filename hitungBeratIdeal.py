from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Content-Type'] = 'application/json'
    response.headers['Api-Name'] = 'Math-API'
    response.headers['Server'] = 'Poltek-Harber.io'
    return response

#curl -i -X POST http://127.0.0.1:7092/hitung -d "berat=60&tinggi=175" -H 'Content-Type: application/json'

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

    hasil = {'hasil': bmi, 'keterangan': ket}
    return jsonify(hasil)

if __name__ == '__main__':
   app.run(debug = True, port=7092)
