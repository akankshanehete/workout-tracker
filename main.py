import requests
import datetime

APP_ID = '348bd446'
API_KEY = '/////////////'

query = str(input("What did you do today?: "))

nutritionix_params = {
    "query": query,
    "gender": "female",
    "age": '19'
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote_user_id": '0'
}

nutritionix_response = requests.post('https://trackapi.nutritionix.com/v2/natural/exercise',
                                    json=nutritionix_params,
                                    headers=headers)

exercise_data = nutritionix_response.json()
print(exercise_data)