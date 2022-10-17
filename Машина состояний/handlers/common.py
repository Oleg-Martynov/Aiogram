from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Добро пожаловать! Для старта нажимте НАЧАТЬ (/nickname)",
        reply_markup=ReplyKeyboardRemove()
    )