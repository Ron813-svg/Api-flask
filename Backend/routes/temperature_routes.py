from flask import Blueprint
from controllers.temperature_controller import predict

temperature_bp = Blueprint('temperature', __name__)

temperature_bp.route('/api/predict', methods=['POST'])(predict)
