from flask import Flask
from flask_cors import CORS
from routes.temperature_routes import temperature_bp

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

app.register_blueprint(temperature_bp)

if __name__ == '__main__':
    app.run(debug=True)