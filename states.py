from aiogram.fsm.state import StatesGroup, State



class Place(StatesGroup):
    restaurant = State()
    hotel = State()
    active_chill = State()
    passive_chill = State()
    more = State()