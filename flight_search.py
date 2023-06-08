import requests
from flight_data import FlightData
ENDPOINT = "https://api.tequila.kiwi.com"
API = "Your Api"

class FlightSearch:
    def __init__(self):
        self.head = {"apikey":API}
    def get_destination_codes(self,city_name):
        self.query_endpoint = f"{ENDPOINT}/locations/query"
        self.para = {"term":city_name,"location_types":'city'}

        self.response = requests.get(url=self.query_endpoint,params=self.para,headers=self.head)
        data = self.response.json()
        codes = data["locations"][0]['code']
        return codes
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }

        response = requests.get(
            url=f"{ENDPOINT}/v2/search",
            headers=self.head,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ₹{flight_data.price}")
            return flight_data