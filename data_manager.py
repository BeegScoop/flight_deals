import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")
class DataManager:
    def __init__(self):
        self.header = {
                "Authorization": SHEETY_AUTH
            }
    def make_sheet_request(self):
        response = requests.get(url=SHEETY_ENDPOINT,headers=self.header)
        response.raise_for_status()
        data = response.json()
        return data["prices"]
    def update_rows(self,data):
        for item in data:
            body = {
                "price":item
            }
            print(body)
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{item['id']}",json=body,headers=self.header)
            response.raise_for_status()