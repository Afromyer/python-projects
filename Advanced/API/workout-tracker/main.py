import requests
import datetime as dt
import os

APP_ID = os.getenv("NUTRITIONX_APP_ID")
API_KEY = os.getenv("NUTRITIONX_API_KEY")
TOKEN = os.getenv("SHEETY_TOKEN")
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

nutritionx_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

nutritionx_data = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post(url=nutritionx_endpoint, json=nutritionx_data, headers=headers)
exercises = response.json()["exercises"]

for exercise in exercises:
    name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    today = dt.datetime.now()
    current_date = str(today.date().strftime("%Y/%m/%d"))
    current_time = today.time().strftime("%H:%M:%S")
    body = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url=sheety_endpoint, json=body, headers=headers)
