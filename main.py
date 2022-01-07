import requests
import datetime

APP_ID = '348bd446'
API_KEY = '/////////////'

# query = str(input("What did you do today?: "))

nutritionix_params = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 51,
    "height_cm": 165,
    "age": 19
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote_user_id": '0'
}

nutritionix_response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',
                                    params=nutritionix_params,
                                    headers=headers)
print(nutritionix_response.text)
exercise_data = nutritionix_response.json()
print(exercise_data)