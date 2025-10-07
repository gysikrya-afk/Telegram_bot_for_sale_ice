from aiogram.fsm.state import State,StatesGroup

class Ice(StatesGroup):
    name = State()
    ice = State()
    ice_number = State()
    city = State()
    street = State()
    house = State()
    phone = State()
    email = State()
