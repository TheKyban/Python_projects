import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, endpoint, user):
        self.code = None
        self.json = None
        self.response = None
        self.endpoint = endpoint
        self.authentication = user

    def get_method(self):
        self.response = requests.get(url=self.endpoint, auth=self.authentication)
        return self.response.json()

    def post_method(self, json):
        self.json = json
        self.response = requests.post(url=self.endpoint, auth=self.authentication, json=self.json)
        return self.response.json()

    def put_method(self, json, code):
        self.json = json
        self.code = code
        self.response = requests.put(url=f"{self.endpoint}/{self.code}", auth=self.authentication, json=self.json)
        return self.response.json()
