from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel_button = KeyboardButton('cancel')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(cancel_button)