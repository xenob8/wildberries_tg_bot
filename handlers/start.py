from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

import keyboards
from form import Form

on_start_router = Router()

@on_start_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    # После команды запуска бота должны отображаться справочная информация и кнопки в клавиатуре(reply Markup):
    # мои товары, добавить товар, помощь, обратиться в поддержку
    await state.set_state(Form.menu)
    await message.answer(
        "Здарова, это наш бот тут можно отслеживать товары, нажми на кнопку",
        reply_markup=keyboards.menu_kb,
    )
