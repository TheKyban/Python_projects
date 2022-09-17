import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]

position_iss = (latitude,longitude)
print(position_iss)