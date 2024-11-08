import requests
from twilio.rest import Client
import os

API_KEY = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

parameters = {
    "appid": API_KEY,
    "lat": -26.745742840880094,
    "lon": 27.704934178359903,
    "units": "metric",
    "cnt": 8
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_list = weather_data["list"]

condition_codes = [hour_data["weather"][0]["id"] for hour_data in weather_list]
times = [hour_data["dt_txt"] for hour_data in weather_list]


will_rain = False
rain_time_start = []
for i in range(len(condition_codes)):
    if int(condition_codes[i]) < 700:
        rain_time_start.append(f"-{times[i]}")
        will_rain = True

if will_rain:
    raining_times = "\n".join(rain_time_start)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Rain is expected on:\n{raining_times}\nBring an umbrella☂️",
        from_='+19472227091',
        to='+27680495232'
    )
    print(message.status)
else:
    print("No rain detected")




