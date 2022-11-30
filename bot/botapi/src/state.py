from aiogram.dispatcher.filters.state import State, StatesGroup


class GStates(StatesGroup):
    start = State()
    random_five = State()
    all_words = State()


class Hstates(StatesGroup):
    start = State()
    random_ten = State()
    all_words = State()