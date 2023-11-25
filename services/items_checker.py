from api.api_service import get_product
from db import product_service
from db.product_service import ProductService
from notifier import Notifier
from typing import TypedDict
import time


class Item(TypedDict):
    art: str
    last_price: int


async def check_price_change(item_art, last_price):
    history = await get_product(item_art)
    price = history[0]['salePriceU'] / 100
    if abs(price - last_price) != 0:
        return price


async def check_availability(item_art, last_availability):
    history = await get_product(item_art)
    size = history[0]['sizes']
    availability = False
    if len(size['stocks']):
        availability = True
    return availability != last_availability


class ItemsChecker():
    def __init__(self, notifier: Notifier):
        self.items: list[Item] = []
        self.notifier = notifier

    def check_items(self):
        for item in self.items:
            item_art, last_price = item["art"], item["last_price"]
            new_price = check_price_change(item_art, last_price)
            if new_price:
                self.notifier.notify(item_art, new_price)

    def update(self, freq=60*5):
        product_service = ProductService()
        products = product_service.get_all_product()
        ItemsChecker()
        check_items()
        time.sleep(freq)
