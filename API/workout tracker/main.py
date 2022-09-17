import datetime
import requests
from requests.auth import HTTPBasicAuth

nutritionix_app_id = "e8dea5b3"
nutritionix_app_key = "04b02b67fa72325581e4083f0f59c287"
basic = HTTPBasicAuth(username="kyban", password="adityakumarchaudhary1392")

header = {
    "x-app-id": "e8dea5b3",
    "x-app-key": "04b02b67fa72325581e4083f0f59c287",
    "Content-Type": "application/json"
}
query = {
    "query": input("enter your workout:"),

}
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/8f7850ad0dc531f60d854246f7d85a30/workoutTracking/workouts"

response = requests.post(url=nutritionix_endpoint, headers=header, json=query)
data = response.json()
name = data["exercises"][0]["name"]
calories = data["exercises"][0]["nf_calories"]
duration = data["exercises"][0]["duration_min"]

date = datetime.datetime.now().strftime("%d/%m/%y")
time = datetime.datetime.now().strftime("%H:%M:%S")

json_data = {
    "workout":
        {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories,

        }

}
sheet = requests.post(url=sheet_endpoint,json=json_data, auth=("kyban", "adityakumarchaudhary1392"))
print(sheet.text)
