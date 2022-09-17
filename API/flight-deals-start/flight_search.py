import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):


    def get_destination_code(self, city_name):
        header = {"apikey": "7rwDbrGqwKn5lfLRz6u4KWMh8ZObUtwM"}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=query)
        code = response.json()["locations"][0]["code"]
        return code


city_name = "paris"
flight = FlightSearch()
data = flight.get_destination_code(city_name=city_name)
print(data)


