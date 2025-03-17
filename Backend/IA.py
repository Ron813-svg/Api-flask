from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)


ocult1 = tf.keras.layers.Dense(units=5, input_shape=[1])
ocult2 = tf.keras.layers.Dense(units=6)
exitIA = tf.keras.layers.Dense(units=1)

modelo = tf.keras.Sequential([ocult1, ocult2, exitIA])


modelo.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
modelo.fit(celsius, fahrenheit, epochs=2000, verbose=False)


@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'celsius' not in data:
            raise ValueError("El parámetro 'celsius' es obligatorio.")

        temp_celsius = float(data['celsius'])
        
        
        temp_fahrenheit = modelo.predict([temp_celsius])[0][0]

       
        return jsonify({"fahrenheit": temp_fahrenheit})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Error en el servidor: " + str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
