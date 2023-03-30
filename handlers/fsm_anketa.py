from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.keyboard import cancel_markup
from database.bot_dp import sql_command_insert


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    gruppa = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.id.set()
        await message.answer(f'Приветствую {message.from_user.username}')
        await message.answer(f'ID ментора {message.chat.id}:', reply_markup=cancel_markup)
    else:
        await message.answer('Нельзя делать этого в групе')


async def set_id(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = int(message.chat.id)
        await FSMAdmin.next()
        await message.answer(f'Теперь напишите имя ментора', reply_markup=cancel_markup)
    except:
        await message.answer(f'ID должно состоять только из цирф')


async def set_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer(f'Теперь напишите направление ментора', reply_markup=cancel_markup)


async def set_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer(f'возраст ментора', reply_markup=cancel_markup)


async def set_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            age = int(message.text)
            if 12 <= age <= 60:
                data['age'] = age
            else:
                raise ValueError
        await FSMAdmin.next()
        await message.answer('Введите группу ментора', reply_markup=cancel_markup)
    except:
        await message.answer(f'Неправильный возраст')


async def set_grup(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['grup'] = message.text
        await message.answer(f"ID: {data['id']}\n"
                             f"Имя: {data['name']}\n"
                             f"Направление: {data['direction']}\n"
                             f"Возраст: {data['age']}\n"
                             f"Группа: {data['grup']}"
                             f"все ли правильно?")

    await FSMAdmin.next()

async def submit(message: types.Message, state: FSMContext):
    if message.text == "ДА":
        # Запись в БД
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Ты зареган!")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Ну и иди ты')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands=['cancel'], commands_prefix='/!.')
    dp.register_message_handler(cancel_registration, Text(equals='Cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(set_id, state=FSMAdmin.id)
    dp.register_message_handler(set_name, state=FSMAdmin.name)
    dp.register_message_handler(set_direction, state=FSMAdmin.direction)
    dp.register_message_handler(set_age, state=FSMAdmin.age)
    dp.register_message_handler(set_grup, state=FSMAdmin.gruppa)
    dp.register_message_handler(submit, state=FSMAdmin.submit)