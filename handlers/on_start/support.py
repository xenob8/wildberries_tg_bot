from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import keyboards
from form import Form


support_router = Router()
@support_router.message(Form.menu, F.text.casefold() == '📝 написать в поддержку')
async def add_item(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.support)

    await message.answer(
        f'Сообщение с просьбой оставить комментарий',
        reply_markup=keyboards.return_to_menu_kb
    )


@support_router.message(Form.support)
async def process_msg_to_support(message: Message, state: FSMContext) -> None:
    await state.update_data(support=message.text)
    #пишем разработчикам
    await message.answer('Сообщение о том, что комментарий был отправлен')