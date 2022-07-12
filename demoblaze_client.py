import json
from typing import List

from demoblaze_rest_api import DemoblazeRestApi


class DemoblazeClient:
    def __init__(self, username: str, password: str):
        self.__rest_client = DemoblazeRestApi()
        self.__username: str = username
        self.__password: str = password
        self.__token = self.get_token(username, password)

    def get_token(self, username: str, password: str) -> str:
        self.__token = self.__rest_client.login(username, password).split(" ")[-1].strip("\"\n")
        return self.__token

    def get_cart_items_id_list(self) -> List[str]:
        response: str = self.__rest_client.view_cart(self.__token)
        cart_content: dict = json.loads(response)["Items"]
        items: list = []
        for item in cart_content:
            items.append(item["prod_id"])
        return items

    def get_item_price(self, item_id: str) -> float:
        response = self.__rest_client.view(item_id)
        item = json.loads(response)
        return item["price"]

    def get_item_title(self, item_id: str) -> str:
        response = self.__rest_client.view(item_id)
        item = json.loads(response)
        return item["title"]
