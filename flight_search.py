import os
from dotenv import load_dotenv
import requests
import datetime
load_dotenv()

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")

        self.token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.token = self.get_new_token()

    def find_code(self, name):
        params = {
            "keyword": name,
            "max": "2",
            "include": "AIRPORTS",
        }
        iata_header = {
            "authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=self.iata_endpoint, params=params, headers=iata_header)
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
        response = requests.post(url=self.token_endpoint, headers=token_header, data=token_body)
        response.raise_for_status()
        data = response.json()
        print(data["access_token"])
        print(f"Your token expires in {data['expires_in']} seconds")
        return data["access_token"]

    def get_flights(self, destination_code, origin_code, from_time: datetime, to_time: datetime):
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        query = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            # "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",



        }
        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", headers=header, params=query)
        response.raise_for_status()
        return response.json()
