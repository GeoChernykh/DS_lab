import datetime as dt
import json
import os

import requests
from flask import Flask, jsonify, request

from ..errors import InvalidUsage


# WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
WEATHER_API_KEY = "2AWEHQ2Z5ZA7EBLZQF35K7WXB"


def get_forecast(location, start_date, end_date, unit_group="metric"):
    BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    elements = "datetime,humidity,offset,temp,windspeed,pressure,visibility,severerisk,offsetseconds,cloudcover"
    request_url = f"{BASE_URL}/{location}/{start_date}/{end_date}?unitGroup={unit_group}&key={WEATHER_API_KEY}&include=hours&elements={elements}&lang=en"

    response = requests.get(request_url)

    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    else:
        raise InvalidUsage(response.text, status_code=response.status_code)
    

