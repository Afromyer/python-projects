import requests
from datetime import datetime
import smtplib

MY_LAT = -26.709047039400026  # Your latitude
MY_LONG = 27.8740810298094  # Your longitude

MY_EMAIL = "jpjoubert2006@gmail.com"
MY_PASSWORD = "rwpmavsbnefgxccw"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.

def is_overhead(latitude, longitude):
    if (iss_latitude >= latitude - 5) and (iss_latitude <= latitude + 5) and (iss_longitude >= longitude - 5) and (
            iss_longitude <= longitude + 5):
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if (time_now.hour >= sunset) and (time_now.hour <= sunrise):
        return True
    return False


if is_overhead(MY_LAT, MY_LONG) and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, msg="Subject:LOOK UP\n\nThe ISS is overhead.")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
