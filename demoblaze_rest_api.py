import base64
import json

import requests


class DemoblazeRestApi:
    def __init__(self):
        self.__url = "https://api.demoblaze.com"

    def login(self, username: str, password: str):
        b64_password = base64.b64encode(password.encode("ascii"))
        data_dict: dict = {"username": username, "password": b64_password.decode("utf-8")}
        data_string: str = json.dumps(data_dict)
        token: str = requests.post(f"{self.__url}/login", headers={"Content-Type": "application/json"}, data=data_string).text
        return token

    def view_cart(self, token: str):
        data_dict: dict = {"cookie": token, "flag": True}
        data_string: str = json.dumps(data_dict)
        response = requests.post(f"{self.__url}/viewcart", headers={"Content-Type": "application/json"}, data=data_string)
        return response.text

    def view(self, item_id: str) -> str:
        data_dict: dict = {"id": item_id}
        data_string: str = json.dumps(data_dict)
        response = requests.post(f"{self.__url}/view", headers={"Content-Type": "application/json"}, data=data_string)
        return response.text
