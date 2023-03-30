
from aiogram.utils import executor
import logging

from config import dp
from handlers import client,callback,extra,fsm_anketa
from database.bot_dp import sql_create


async def on_startup(_):
    sql_create()

callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
fsm_anketa.register_handlers_fsm(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
