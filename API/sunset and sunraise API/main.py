import requests
parameters = {
    "lat":26.110979,
    "lng":85.334846,
    "formatted":0,
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status
data = response.json()["results"]
sunrise = data["sunrise"].split("T")[1].split(":")[0:2]
sunset = data["sunset"].split("T")[1].split(":")[0:2]

print(sunrise)
print(sunset)