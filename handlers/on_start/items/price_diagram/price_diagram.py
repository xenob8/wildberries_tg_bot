from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto, URLInputFile, message
from aiogram.utils.markdown import hide_link

import keyboards

from handlers.router import router


@router.callback_query(F.data.startswith('price_diagram'))
async def price_diagram(callback: CallbackQuery):
    url = get_diagram()
    await callback.message.edit_text(f"{hide_link(url)}График изменения цены товара",
                                     reply_markup=keyboards.return_to_card_item_kb)


def get_diagram():
    return "https://hr-portal.ru/files/mini/analiz1.jpg"
