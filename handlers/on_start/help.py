from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputFile
from aiogram.utils.markdown import hide_link

import keyboards
from form import Form

from handlers.router import router


@router.message(Form.menu, F.text.casefold() == '❓ помощь')
async def my_items(message: Message, state: FSMContext) -> None:
    await message.answer(
        f"Список функций бота и их объяснение"
    )
