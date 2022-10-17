from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from quiz_state import QuizState

router = Router()

programmingLanguages = ['Python', 'C++', 'Java']


@router.message(Command(commands=['nickname']))
async def startReg(message: Message, state: FSMContext):
    await message.answer('Введите nickname')
    await state.set_state(QuizState.nickname)


@router.message(QuizState.nickname)
async def getNickname(message: Message, state: FSMContext):
    await state.update_data(nickname=message.text.lower())
    await message.answer('Введите год рождения')
    await state.set_state(QuizState.birthYear)


@router.message(QuizState.birthYear)
async def getBirthYear(message: Message, state: FSMContext):
    await state.update_data(birthYear=message.text.lower())
    row = [KeyboardButton(text=item) for item in programmingLanguages]
    languageKeyboard = ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выберите язык программирования:",
        reply_markup=languageKeyboard
    )
    await state.set_state(QuizState.progLanguage)


@router.message(QuizState.progLanguage)
async def getProgLanguage(message: Message, state: FSMContext):
    await state.update_data(progLanguage=message.text.lower())
    data = await state.get_data()
    await message.answer(
        text=f"{data['nickname']}\n{data['birthYear']}\n{data['progLanguage']}",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()