#This class is responsible for talking to the Google Sheet.
import requests

class DataManager:
    def __init__(self):
        self.sheety_endpoint = "your endpoint url"
        self.destination_data = {}
    def get_destination_data(self):
        response = requests.get(url=self.sheety_endpoint)
        data = response.json()
        self.destination_data = data['prices']

        return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

