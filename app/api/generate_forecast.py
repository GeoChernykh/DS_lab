from flask import Blueprint, jsonify
from app.errors import InvalidUsage
from app.core.model_scripts.lgbm_predict import generate_forecast

generate_forecast_bp = Blueprint('generate_forecast', __name__)


@generate_forecast_bp.route('/generate_forecast', methods=['GET'])
def generate_forecast_endpoint():
    try:
        result = generate_forecast(save_to_file=True)
        return jsonify(result)
    except FileNotFoundError as exc:
        raise InvalidUsage(str(exc), status_code=500)
    except Exception as exc:
        raise InvalidUsage(f'Forecast generation failed: {exc}', status_code=500)
