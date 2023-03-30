from aiogram import Bot,Dispatcher
from  decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage



TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

ADMIN = (763112308, )