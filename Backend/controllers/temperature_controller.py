from flask import request, jsonify
from models.temperature_model import modelo
import numpy as np


def predict():
    try:
        data = request.get_json(force=True, silent=True)
        print("Data recibida:", data)  


        if not data or 'celsius' not in data:
            raise ValueError("El parámetro 'celsius' es obligatorio.")

        temp_celsius = float(data['celsius'])
        resultado = modelo.predict(np.array([[temp_celsius]]))
        temp_fahrenheit = float(resultado[0][0])

        return jsonify({"fahrenheit": float(temp_fahrenheit)})

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Error en el servidor: " + str(e)}), 500
