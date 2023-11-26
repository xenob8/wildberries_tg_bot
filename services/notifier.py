from sqlalchemy.orm import Session
from handlers import router
from main import bot
from db.product_service import ProductService

@router.message()
def notify(item_art, new_val, session: Session, product_service: ProductService):
    positions = product_service.get_users_of_product(item_art, session)
    for item in positions:
        if item.start_price > new_val:
            bot.send_message(item.user_telegram_id, "Цена понизилась")
        elif item.start_price < new_val:
            bot.send_message(item.user_telegram_id, "Цена повысилась")


@router.message()
def notify(item_art, new_availability, session: Session, product_service: ProductService):
    positions = product_service.get_users_of_product(item_art, session)
    for item in positions:
        if new_availability:
            bot.send_message(item.user_telegram_id, "Товар появился в наличии")
        else:
            bot.send_message(item.user_telegram_id, "Товар не в наличии")
