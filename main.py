#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime

ORIGIN_CITY_IATA = "PHX"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.make_sheet_request()

for item in sheet_data:
    if item["iataCode"] == "":
        item["iataCode"] = flight_search.find_code(item["city"])
# data_manager.update_rows(sheet_data)

today = datetime.datetime.now()
tomorrow = today+datetime.timedelta(days=1)
in_six_months = tomorrow+datetime.timedelta(days = 182)

for destination in sheet_data:
    print(f"Getting flights for {destination["city"]}")
    flights = flight_search.get_flights(
        destination["iataCode"],
        ORIGIN_CITY_IATA,
        from_time=tomorrow,
        to_time=in_six_months
    )
    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_notification(cheapest_flight.price,cheapest_flight.origin_airport,cheapest_flight.destination_airport,cheapest_flight.out_date,cheapest_flight.return_date)