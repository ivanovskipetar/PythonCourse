import requests, os
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
# print(response.text)

PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20240103"
pixel_update_data = {
    "quantity": "3.65",
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=pixel_update_data, headers=headers)
# print(response.text)

PIXEL_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20240103"
response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
print(response.text)