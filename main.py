from data_manager import DataManager
from datetime import datetime,timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_Data = data_manager.get_destination_data()
flight_search = FlightSearch()
notificationmanger = NotificationManager()

ORIGIN_CITY_IATA = "DEL"
if sheet_Data[0]["iataCode"] == "":
    for row in sheet_Data:
        row["iataCode"] = flight_search.get_destination_codes(row["city"])
    print(f"Sheet_Data:\n {sheet_Data}")

    data_manager.destination_data = sheet_Data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_Data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue
    if flight.price < destination["lowestPrice"]:
        message = str(f"Low price alert! Only ₹{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.")
        link = f"https://www.google.co.in/flights?hl=en&flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        if flight.stop_overs > 0:
            message += f"\nFlight has ruppe {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        notificationmanger.send_msg(message)
        notificationmanger.send_email(message,link)

    