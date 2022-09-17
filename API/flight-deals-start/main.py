# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
sheet_endpoint = "https://api.sheety.co/8f7850ad0dc531f60d854246f7d85a30/flightDeals/deals"
authentication = ("kyban", "adityakumarchaudhary1392")
data_json = {
    "deal": {
        "city": "patna",
        "iataCode": "53",
        "lowestPrice": "66",
    }
}

data_manager = DataManager(sheet_endpoint, authentication)
data = data_manager.get_method()
print(data)