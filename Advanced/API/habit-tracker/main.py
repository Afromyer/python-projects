import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "jpjoubert"
TOKEN = "kjDSF2fW335LoS3n"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

GRAPH_ID = "learntracker1"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Daily Learning Tracker",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = dt.datetime(year=2024, month=9, day=24)

graph_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3"
}

response = requests.post(url=f"{graph_endpoint}/learntracker1", json=graph_pixel_config, headers=headers)
print(response.text)
