import datetime

from aiogram import Bot
from database.bot_dp import sql_command_get_id_name
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from config import bot, ADMIN


async def napominanie(bot: Bot):
    users = await sql_command_get_id_name()
    for user in users:
        await bot.send_message(user[0], f"Сегодня Жума! {user[1]}")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    # scheduler.add_job(
    #     go_to_sleep,
    #     trigger=CronTrigger(
    #         hour=20,
    #         minute=55,
    #         start_date=datetime.datetime.now()
    #     ),
    #     kwargs={"bot": bot}
    # )

    scheduler.add_job(
        napominanie,
        trigger=DateTrigger(
            run_date=datetime.datetime(
                year=2023, month=3, day=30, hour=16, minute=51, second=0
            )
        ),
        kwargs={"bot": bot}
    )

    scheduler.start()