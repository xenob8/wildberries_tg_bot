import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict
from db.models.base import Base
from db.models.product import Product
from db.models.user import User
from db.models.user_product import UserProduct

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from sqlalchemy import create_engine

import config
from db.product_service import ProductService
from middleware.service_middleware import CounterMiddleware, ServiceMiddleware

# from handlers.on_start.add_item import add_item_router

TOKEN = config.TOKEN
print(TOKEN)

DATABASE_URL = f"postgresql://dyvawvhc:{config.bd_pass}@trumpet.db.elephantsql.com/dyvawvhc"

engine = create_engine(DATABASE_URL)

form_router = Router()
form_router.message.middleware(ServiceMiddleware(engine))


class Form(StatesGroup):
    name = State()
    like_bots = State()
    language = State()


@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext, product_service: ProductService) -> None:
    print("exists?")
    print(product_service.product_exists_by_number(1))
    #После команды запуска бота должны отображаться справочная информация и кнопки в клавиатуре(reply Markup):
    # мои товары, добавить товар, помощь, обратиться в поддержку
    # await state.set_state(Form.name)
    # print(message)
    await message.answer(
        "Hi there! What's your name?",
        reply_markup=ReplyKeyboardRemove(),
    )

async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(form_router)


    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())