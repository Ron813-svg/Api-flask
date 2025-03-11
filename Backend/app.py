from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/saludo', methods=['GET'])

def saludo():
    return jsonify({"Mensaje": "Hola mundo"})

@app.route('/api/suma', methods=['POST'])
def suma():
    data = request.get_json
    requestResult = data['num1'] + data['num2']
    return jsonify({"Resultado": requestResult})

if __name__ == '__main__':
    app.run(debug=True)