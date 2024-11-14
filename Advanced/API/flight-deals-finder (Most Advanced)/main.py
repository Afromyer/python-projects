#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests.exceptions

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import datetime as dt
import time

ORIGIN_LOCATION_IATA = "JNB"
message = ""

# Checks if there are any data that can be sent to the user's email
has_flight_data = False

sheet = DataManager()

prices_sheet_data = sheet.get_table_data("prices")
user_data = sheet.get_table_data("users")["users"]

tomorrow = (dt.datetime.today() + dt.timedelta(days=1)).strftime("%Y-%m-%d")
return_date = ((dt.datetime.today() + dt.timedelta(days=1) + dt.timedelta(days=30)).strftime("%Y-%m-%d"))

for row in prices_sheet_data["prices"]:
    flight = FlightSearch(row["city"])
    lowest_price = row["lowestPrice"]

    # Checks if each row as an IATA code
    if row["iataCode"] == "":
        sheet.update_row(row["id"], "iataCode", flight.get_city_iata_code())
        print("Trying to create IATA code, restart program after everything was created")
    # Gives time for the Google sheet to update with the generated IATA Code

    print(f"Getting cheapest price for {row["city"]}...")

    # Checks if an IATA could be generated
    try:
        current_flight_data = flight.get_flight_data(ORIGIN_LOCATION_IATA, row["iataCode"], tomorrow, return_date)
    except requests.exceptions.HTTPError:
        print("No IATA could be generated")
        print("")
    else:
        flight_data = FlightData(None,None,None,None, None)

        # Flight Data of the cheapest flight found
        flight_data = flight_data.get_cheapest_flight(current_flight_data)
        try:
            if flight_data.price != "N/A":
                if float(flight_data.price) < lowest_price:
                    message = message + f"""Low Price Alert!🔻
Only {"R{:,.2f}".format(flight_data.price)} to fly from {flight.get_airport_name(flight_data.origin_airport)} to {flight.get_airport_name(flight_data.destination_airport)} on {flight_data.out_date} until {flight_data.return_date}.\n\n"""
                    has_flight_data = True
                    print("Flight Data was found and will be sent to the users")
                else:
                    print("Cheaper price than specified not found")
        except ValueError:
            raise
        finally:
            print("")

if has_flight_data:
    notification = NotificationManager()
    for user in user_data:
        user_email = user["email"]
        notification.send_email(user_email, message.encode('ascii', 'ignore').decode('ascii'))

