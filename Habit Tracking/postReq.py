import requests
from datetime import datetime

USERNAME = 'timberman'
TOKEN = 'trackyourhabitmf'
GRAPH_ID = "graph69"

pixels_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs"
pixel_creation_endpint = f'{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

user_params = {
    'token':TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixels_endpoint,json=user_params, verify=False)
# print(response.text) # Created the user

graph_config = {
    'id': 'graph69',
    'name': 'Workout Habit',
    'unit': 'hr',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers, verify=False)
# print(response.text) # Request made

now = str(datetime.now())
now_split = (now.split(" ")[0]).replace('-','')



request_body = {
    'date': now_split,
    'quantity': '1.5',
}

response = requests.post(url=pixel_creation_endpint, json=request_body, headers=headers, verify=False)
print(response.text)