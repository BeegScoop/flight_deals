#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_data = FlightData()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.make_sheet_request()

for item in sheet_data:
    if item["iataCode"] == "":
        item["iataCode"] = flight_search.find_code(item["city"])
data_manager.update_rows(sheet_data)
