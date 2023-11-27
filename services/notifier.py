from db.product_service import ProductService
from aiogram import Bot


async def notify(item_art, new_val: float, product_service: ProductService, bot: Bot):
    positions = await product_service.get_users_of_product(item_art)
    for item in positions:
        threshold = item.alert_threshold
        if item.start_price:
            if (1 + threshold) * item.start_price > new_val:
                text = "Цена понизилась на " + str(new_val - item.start_price)
                await bot.send_message(item.user_telegram_id, text)
            elif item.start_price < (1 + threshold) * new_val:
                text = "Цена понизилась на " + str(item.start_price - new_val)
                await bot.send_message(item.user_telegram_id, text)


async def notify_avail(item_art, new_availability, product_service: ProductService, bot: Bot):
    positions = await product_service.get_users_of_product(item_art)
    for item in positions:
        if item:
            if new_availability:
                await bot.send_message(item.user_telegram_id, "Товар появился в наличии")
            else:
                await bot.send_message(item.user_telegram_id, "Товар не в наличии")