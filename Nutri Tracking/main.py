import requests
import warnings
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
warnings.filterwarnings(action='ignore')

APPLICATION_ID = os.environ.get('APPLICATION_ID')
APPLICATION_KEY = os.environ.get('APPLICATION_KEY')
GENDER = 'male'
WEIGHT = 56
HEIGHT = 167.64
AGE = 20
now = str(datetime.now())
TODAY_DATE = now.split(" ")[0]
TODAY_TIME = now.split(" ")[1][:5]

exercise_endpoints = os.environ.get('exercise_endpoints')
sheety_endpoints = os.environ.get('sheety_endpoints')

user_query = input("Enter the query: ")

headers = {
    'x-app-id': APPLICATION_ID,
    'x-app-key': APPLICATION_KEY,
}

parameters = {
    'query': user_query,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}

response = requests.post(url= exercise_endpoints, json=parameters, headers=headers)
result = response.json()
print(result)

for exercise in result['exercises']:

    body_sheety = {
        'workout':{
            'date': TODAY_DATE,
            'time': TODAY_TIME,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheety_response = requests.post(url=sheety_endpoints, json=body_sheety)

    print(sheety_response.text)