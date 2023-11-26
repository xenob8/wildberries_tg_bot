from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from db.user_product_service import UserProductService
from form import Form

from handlers.router import router


@router.callback_query(F.data.startswith('update_tracking'))
async def update_tracking_price(callback: CallbackQuery, user_service: UserProductService):
    number = callback.data.split('update_tracking_')[1]
    user_service.patch_start_price(callback.from_user.id, number)
    await callback.answer('Цена успешно изменена')
