from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputFile
from aiogram.utils.markdown import hide_link

import keyboards
from form import Form

my_items_router = Router()


@my_items_router.message(Form.menu, F.text.casefold() == '🛍 мои товары')
async def my_items(message: Message) -> None:
    my_items = get_items(message.from_user.id)
    if my_items is None:
        await message.answer(
            'Вы еще ничего не добавили'
        )
    else:
        for item in my_items:
            await message.answer(
                f"{hide_link('https://fikiwiki.com/uploads/posts/2022-02/1645036029_47-fikiwiki-com-p-kartinki-znachki-49.png')}"
                f"{item}",
                reply_markup=keyboards.item_card_available_kb
            )


def get_items(user_id):
    # Запрос к базе
    return ["Название товара\nИзначальная цена товара:\nПоследняя измененная цена товара:\nРазница в цене:\n"
            "Текущий порог оповещения:\n"]
