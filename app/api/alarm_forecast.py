import json
from flask import Blueprint, jsonify
from app.errors import InvalidUsage
from app.core.model_scripts.lgbm_predict import generate_forecast
from pathlib import Path
import datetime as dt


forecast_dir = Path("data/predictions")

alarm_forecast_bp = Blueprint('alarm_forecast', __name__)


@alarm_forecast_bp.route('/forecast', methods=['GET'])
def forecast():
    curr_dt = dt.datetime.now()
    file_name = f"alarm_forecast_{curr_dt.strftime('%Y%m%d%H00')}.json"
    forecast_path = forecast_dir / file_name

    if not forecast_path.exists():
        # try:
        #     result = generate_forecast(save_to_file=True)
        #     return jsonify(result)
        # except Exception as exc:
        #     print(f"Forecast generation failed: {exc}")

        prev_hour_dt = curr_dt - dt.timedelta(hours=1)
        file_name = f"alarm_forecast_{prev_hour_dt.strftime('%Y%m%d%H00')}.json"
        forecast_path = forecast_dir / file_name

    if not forecast_path.exists():
        raise InvalidUsage('Forecast data not available', status_code=404)

    with open(forecast_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)
