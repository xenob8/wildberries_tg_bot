from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from form import Form

from handlers.router import router


@router.callback_query(F.data == 'stop_tracking')
async def stop_tracking_item(callback: CallbackQuery):
    stop_tracking()
    await callback.message.edit_text('Вы больше не отслеживаете этот товар')
    await callback.message.delete_reply_markup()


def stop_tracking():
    pass
