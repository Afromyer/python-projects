import requests
import os

API_KEY = os.getenv("AMADEUS_API_KEY")
API_SECRET = os.getenv("AMADEUS_API_SECRET")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.flight_offer_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.airport_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations"
        self.auth_token = self.get_auth_token()
        self.auth_header = {
            "Authorization": f"Bearer {self.auth_token}"
        }

    def get_auth_token(self):
        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }
        token_data = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }

        response = requests.post(self.token_endpoint, data=token_data, headers=headers)

        bearer_token = response.json()["access_token"]
        return bearer_token

    def get_city_data(self):
        search_parameters = {
            "keyword": self.city,
            "include": ["AIRPORTS"]
        }

        response = requests.get(self.city_search_endpoint, params=search_parameters, headers=self.auth_header)
        city_data = response.json()
        return city_data

    def get_city_iata_code(self):
        try:
            city_data = self.get_city_data()["data"]
            return city_data[0]["iataCode"]
        except IndexError:
            return ""
        except KeyError:
            return ""

    # def get_city_airport_data(self):
    #     city_data = self.get_city_data()
    #     airport_data = city_data["included"]["airports"]
    #     return airport_data

    def get_flight_data(self, origin_iata, destination_iata, depart_date, return_date):
        offer_parameters = {
            "originLocationCode": origin_iata,
            "destinationLocationCode": destination_iata,
            "departureDate": depart_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "ZAR",
            "max": "250"
        }

        response = requests.get(url=self.flight_offer_endpoint, params=offer_parameters, headers=self.auth_header)
        response.raise_for_status()
        return response.json()

    def get_airport_name(self, airport_iata_code):
        try:
            response = requests.get(url=f"{self.airport_endpoint}/{airport_iata_code}", headers=self.auth_header)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return airport_iata_code

        data = response.json()
        airport_name = data["data"]["name"]
        return airport_name












