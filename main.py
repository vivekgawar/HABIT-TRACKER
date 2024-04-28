import requests
from datetime import datetime

USERNAME = "crimsonbully"
TOKEN = "afhb789h3wq987thf87934s"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph69",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime(year=2023, month=8, day=7)

########POSTING PIXEL##########

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph69"

value_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.9"
}
response = requests.post(url=pixel_creation_endpoint, json=value_config, headers=headers)
print(response.text)

########UPDATE PIXEL##########

update_pixel_endpoint = f"{pixela_endpoint}/crimsonbully/graphs/graph69/{today.strftime('%Y%m%d')}"
updated_value = {
    "quantity": "5"
}

response_update = requests.put(url=update_pixel_endpoint, json=updated_value, headers=headers)
print(response_update.text)

########DELETE PIXEL##########

delete_pixel_endpoint = f"{update_pixel_endpoint}"
delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(delete_response.text)
