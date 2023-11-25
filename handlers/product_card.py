from aiogram.utils.markdown import hide_link


def get_card(link, title, start_price, last_price, diff_price, treshhold):
    return f"{hide_link(link)}Название товара: {title}\n" \
           f"Изначальная цена товара: {start_price}\nПоследняя измененная цена товара: {last_price}\n" \
           f"Разница в цене: {diff_price}\nТекущий порог оповещения: {treshhold}\n"
