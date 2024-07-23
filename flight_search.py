import os
from dotenv import load_dotenv
import requests
class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")

        self.token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.flight_endpoint = "test.api.amadeus.com/v2/shopping/flight-offers"
        self.token = self.get_new_token()
    def find_code(self,name):
        params = {
            "keyword":name
        }
        iata_header = {
            "authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=self.iata_endpoint,params=params,headers=iata_header)
        response.raise_for_status()
        data = response.json()

        return data["data"][0]["iataCode"]
    def get_new_token(self):
        token_header = {
            "content-type": "application/x-www-form-urlencoded"
        }
        token_body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=self.token_endpoint,headers=token_header,data=token_body)
        response.raise_for_status()
        data = response.json()
        return data["access_token"]
    def get_flights(self, iataCode):
        header = {
            "authorization": f"Bearer {self.token}"
        }
        query = {
            "originLocationCode": "PHX",
            "destinationLocationCode":iataCode

        }
        response = requests.get(url=self.flight_endpoint,headers=header, )