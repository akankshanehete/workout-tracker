import requests
import datetime

APP_ID = '348bd446'
API_KEY = '////////////////'

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

exercise_data = nutritionix_response.json()['exercises']
print(exercise_data)

today = str(datetime.date.today().strftime("%d/%m/20%y"))
current_time = str(datetime.datetime.now().strftime('%H:%M:%S'))

for exercise in exercise_data:
    sheety_params = {
        'workout' : {
        'date' : today,
        'time' : current_time,
        'exercise' : exercise['user_input'].title(),
        'duration' : exercise['duration_min'],
        'calories' : exercise['nf_calories']
        }
    }
    sheety_response = requests.post('https://api.sheety.co/ee9e56905dabfef98cb248dacc06b32a/myWorkouts/workouts',
                                    json=sheety_params)
print(sheety_response.text)


