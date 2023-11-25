from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import keyboards

from handlers.router import router


@router.callback_query(F.data.startswith('to_card'))
async def back_to_item_from_diagram(callback: CallbackQuery):
    await callback.message.edit_text(f'тут кароче карточку наверн отрисовываем',
                                     reply_markup=keyboards.item_card_available_kb())
