# SQL - Structured Query Language
# СУБД - Система Управления Базой Данных
import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute(
        "CREATE TABLE IF NOT EXISTS mentors "
        "(id INTEGER PRIMARY KEY, name TEXT, "
        "direction TEXT, age INTEGER, "
        "gruppa TEXT)"
    )
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES (?, ?, ?, ?, ?)",
                       tuple(data.values()))
        db.commit()


async def sql_command_random():
    random_user = cursor.execute("SELECT * FROM anketa ORDER BY random()").fetchone()
    return random_user


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (id,))
    db.commit()