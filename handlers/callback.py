from aiogram import types,  Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import bot,dp

@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Сколько дней в году?"
    answers = [
        "123",
        "365",
        "666",
        "32",
        "БЕССКОНЕЧНОСТЬ",
        "-3",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):

    question = "Король животных?"
    answers = [
        "Медведь",
        "Тигр",
        "Лев",
        "Акула",
        "Горилла",
        "Скунс",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="как так можно?",
        open_period=10,
    )

  #  async def complete_delete(call: types.CallbackQuery):
   #     await sql_command_delete(call.data.replace('delete ', ''))
  #      await call.answer(text='Удален из БД', show_alert=True)
  #      await bot.delete_message(call.message.chat.id, call.message.message_id)

def register_handlers_callback(dp:Dispatcher):
    dp.register_callback_query_handler(quiz_2,text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")
#    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))
    