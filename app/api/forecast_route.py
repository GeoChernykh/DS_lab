from flask import Blueprint, request, jsonify
import datetime as dt

from ..errors import InvalidUsage
from ..core.forecast import get_forecast


forecast_bp = Blueprint("forecast", __name__, url_prefix="/forecast")


@forecast_bp.route("/tomorrow", methods=["GET"])
def get_forecast_endpoint():
    if not request.is_json:
        raise InvalidUsage("JSON body required", status_code=400)

    json_data = request.get_json() or {}

    if json_data.get("location") is None:
        raise InvalidUsage("location required", status_code=400)
    
    location = json_data.get("location")

    curr_datetime = dt.datetime.now()
    start_date = curr_datetime.date()
    end_date = start_date + dt.timedelta(days=1)

    responce = get_forecast(location=location, start_date=start_date, end_date=end_date)

    days = (responce.get("days"))
    hours = []
    for day in days:
        hours.extend(day.get("hours"))

    hours = hours[curr_datetime.hour:(curr_datetime.hour + 24)]

    forecast = dict()

    for hour in hours:
        datetime = hour.pop("datetime")
        h = int(datetime[:2])
        if h >= curr_datetime.hour:
            datetime = f"{str(start_date)} {datetime}"

        else:
            datetime = f"{str(end_date)} {datetime}"

        forecast[datetime] = hour

    return jsonify(forecast)