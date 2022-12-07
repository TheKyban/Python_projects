import smtplib
import requests
endpoint = "https://api.openweathermap.org/data/2.5/weather"
my_email = "sfskfskflkf"
my_pass = "skafksafk"
weather_parameter = {
"lat" : 26.110979,
"lon" : 85.334846,
"exclude" : "hourly,daily",
"appid" : "c890115fc552cb0095dbdeb7d9af827a",
}

response = requests.get(endpoint,params=weather_parameter)
weather = response.json()["weather"]
# print(response)
print(weather)
# weather = 666


# if weather < 700:
#     with smtplib.SMTP("smtp.google.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email,password=my_pass)
#         connection.sendmail(from_addr=my_email, to_addrs="aaditya1392@gmail.com", msg="bring an umbrella")
#         print("sent")

