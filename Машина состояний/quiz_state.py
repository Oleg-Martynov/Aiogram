from aiogram.fsm.state import StatesGroup, State


class QuizState(StatesGroup):
    nickname = State()
    birthYear = State()
    progLanguage = State()
