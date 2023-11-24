from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import keyboards
from handlers.router import router


@router.callback_query(F.data.startswith('diff_'))
async def update_treshhold_to_n(callback: CallbackQuery):
    percent = callback.data.split("_")[1]
    if percent == 'always':
        await callback.message.edit_text(f'тут кароче карточку наверн отрисовываем порог: оповещать всегда',
                                         reply_markup=keyboards.item_card_available_kb)
    else:
        await callback.message.edit_text(f'тут кароче карточку наверн отрисовываем порог: {percent}%',
                                         reply_markup=keyboards.item_card_available_kb)
    await callback.answer(f'Порог успешно изменен')


