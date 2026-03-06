import datetime as dt
from dotenv import load_dotenv
import os

import requests

from app.errors import InvalidUsage

load_dotenv()

ALARM_API_KEY = os.getenv("ALARM_API_KEY")


def get_alarm_status():
    """Fetch raw alarm data from Ukraine Alarm API.

    Returns a list of alerts if successful, or an empty list if request fails
    or response is not valid JSON.
    """
    BASE_URL = "https://api.ukrainealarm.com/api/v3/alerts"

    headers = {
        "Authorization": f"{ALARM_API_KEY}",
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    }

    try:
        response = requests.get(BASE_URL, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError):
        return []


if __name__ == "__main__":
    print(get_alarm_status())