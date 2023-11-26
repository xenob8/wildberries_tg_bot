from api.api_service import get_product
from db import product_service
from db.dto.ProductUpdateDto import ProductUpdateDto

from db.product_service import ProductService
from notifier import Notifier
from typing import TypedDict
import time

from services import notifier


async def check_price_change(item_art):
    history = await get_product(item_art)
    price = history[0]['salePriceU'] / 100
    return price


async def check_availability(item_art):
    history = await get_product(item_art)
    size = history[0]['sizes']
    availability = False
    if len(size['stocks']):
        availability = True
    return availability


async def update(engine, session, freq=60 * 5):
    product_service = ProductService(engine)
    products_from_bd = product_service.get_all_product()  ##продукты из бд
    for product in products_from_bd:
        product_art, product_price, product_avail = product.number, product.price, product.availability
        availability_from_api = await check_availability(product_art)
        price_from_api = await check_price_change(product_art)
        if product_price != price_from_api:
            new_product = ProductUpdateDto(price=price_from_api)
            product_service.patch_product(product_art, new_product, session)
            notifier.notify(product_art, price_from_api, product_price)
        if product_avail != availability_from_api:
            new_product = ProductUpdateDto(availability=availability_from_api)
            product_service.patch_product(product_art, new_product, session)
            notifier.notify(product_art, availability_from_api, product_avail)
    time.sleep(freq)

