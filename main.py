import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(".env")  # loads the environment file

password_nutritionx = os.getenv("PASSWORD_NUTRITIONX")
APP_ID = os.getenv("NUTRITIONX_APP_ID")
API_KEY = os.getenv("NUTRITIONX_API_KEY")


# Nutritionix API
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

parameters = {
    # "query": "I ran 3 miles",
    "query": input("What have you done today ?\n"),
    "gender": "male",
    "weight_kg": 60.00,
    "height_cm": 180.00,
    "age": 24
}

response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)  # make a POST request
print(response.text)
nutrition_data = response.json()

# Extract information from the response
duration = nutrition_data["exercises"][0]['duration_min']
exercise_name = nutrition_data["exercises"][0]['name'].title()
calories = nutrition_data["exercises"][0]['nf_calories']


# Sheety API

sheety_endpoint = "https://api.sheety.co/c0854328a6f925346dcf031765b3dd2c/workoutTracking/workouts"

current_day = datetime.now()
formatted_date = current_day.strftime(f"%d/%m/%Y")
current_hour = current_day.strftime("%H:%M:%S")
print(current_hour)


header_sheety = {
    'Content-Type': 'application/json',
    'Authorization': '*************'
}

sheety_row = {
    "workout": {
         "date": formatted_date,
         "time": current_hour,
         "exercise": exercise_name,
         "duration": duration,
         "calories": calories
     }
}

response = requests.post(url=sheety_endpoint, headers=header_sheety, json=sheety_row)  # sends info about workout
print(response.text)
