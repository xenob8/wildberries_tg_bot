from typing import TypedDict
import time

class UserItem(TypedDict):
    telegram_id: str
    last_price: int




class Notifier():
    def __init__(self):
        pass

    def update(self, check_freq=5*60):
        print(1)

    def notify(self, item_art, new_val):
        pass
