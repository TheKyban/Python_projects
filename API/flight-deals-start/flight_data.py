import requests
import datetime

endpoint = "https://tequila-api.kiwi.com/v2/search"

header = {"apikey": "7rwDbrGqwKn5lfLRz6u4KWMh8ZObUtwM"}

today_date = datetime.datetime.now()
to_date = today_date + datetime.timedelta(days=120)
today_date = today_date.strftime("%d/%m/%y")
to_date = to_date.strftime("%d/%m/%y")

params = {
    "fly_from": "LGA",
    "fly_to": "MIA",
    "dateFrom": today_date,
    "dateTo": to_date,
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "flight_type": "round",
    "one_for_city": 1,
    "max_stopovers": 0,
    "curr": "GBP"

}


class FlightData:
    # This class is responsible for structuring the flight data.
    def get_flight_data(self):
        response = requests.get(url=endpoint, headers=header, params=params)
        print(response.json())


flight = FlightData().get_flight_data()
