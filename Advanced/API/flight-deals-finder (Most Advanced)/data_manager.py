import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/09a4fd405c132536de71e134fd8b94a8/flightDeals"

    def get_table_data(self, table):
        """
        :param table: "prices" or "users"
        :return: Table data in json format
        """

        response = requests.get(url=f"{self.sheety_endpoint}/{table.lower()}")
        return response.json()

    def get_row_amount(self, table):
        data = self.get_table_data(f"{self.sheety_endpoint}/{table.lower()}")
        return len(data["prices"])

    def get_all_row_ids(self, table):
        data = self.get_table_data(f"{self.sheety_endpoint}/{table.lower()}")
        row_ids = [row_dict["id"] for row_dict in data["prices"]]
        return row_ids

    def update_row(self, row_id, column, value):
        update_url = f"{self.sheety_endpoint}/prices/{row_id}"
        body = {
            "price": {
                column: value
            }
        }
        requests.put(url=update_url, json=body)

    def add_user(self, first_name, last_name, email):
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(f"{self.sheety_endpoint}/users", json=body)
        response.raise_for_status()
        print(f"User: {first_name} {last_name} added successfully")

