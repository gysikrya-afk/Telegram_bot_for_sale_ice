from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='О нас')],
        [KeyboardButton(text='Виды льда')],
        [KeyboardButton(text='Заказать лёд')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

menu_result = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Узнать мои данные')],
        [KeyboardButton(text='Повторно написать форму')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
