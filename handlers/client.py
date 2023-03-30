from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ParseMode
from config import bot,dp
from database.bot_dp import sql_command_random
from parserr.cars import parser


#@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Рад приветсвовать! {message.from_user.full_name}"
    )

#@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/мем-1.jpg','rb')
    await bot.send_photo(message.chat.id, photo=photo)

#@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = 'Где проходил Чемпионат Мира по Футболлу 2022?'
    answers = [
        'Бразилия',
        'Катар',
        'Россия',
        'Уругвай',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )



async def get_random_mentor(message: types.Message):
    await sql_command_random(message)


async def parsser_wheels(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,

            f"{item['link']}"
            f"{item['logo']}\n"
            f"# {item['size']}\n"
            f"цена - {item['price']}\n"
            )

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(start_command,commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(parsser_wheels, commands=['cars'])