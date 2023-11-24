from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from form import Form

from handlers.router import router


@router.callback_query(F.data == 'update_tracking')
async def update_tracking_price(callback: CallbackQuery):
    change_price_to_last()
    await callback.answer('Цена успешно изменена')


def change_price_to_last():
    pass
