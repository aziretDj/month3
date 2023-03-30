from aiogram import types, Dispatcher
from config import bot, dp


# noinspection PyTypeChecker

async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text) * int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)

    if message.text.startswith('.'):
        await message.pin()

    if message.text.startswith('game'):
        await message.answer_dice()


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
