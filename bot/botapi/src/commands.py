from aiogram import types
from keyboard import inline_keyboard
from app import dp, bot
import messages
from state import GStates, Hstates
from data_fetcher import get_random
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(messages.HELP_MESSAGE)



@dp.message_handler(commands='train_five', state='*')
async def train_five(message: types.Message, state: FSMContext):
    await GStates.random_five.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('gender')
        data['word'] = res.get('word')

        await message.reply(f"{data['step']} из 5, Слово - {data['word']}", reply_markup=inline_keyboard)




@dp.callback_query_handler(lambda x: x.data in ['Male', 'Female', 'Med'], state=GStates.random_five)
async def button_on_click(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data['answer']:
            res = await get_random()
            data['step'] += 1
            data['answer'] = res.get('gender')
            data['word'] = res.get('word')

            if data['step'] > 5:
                await bot.send_message(callback_query.from_user.id, "Все ответы верные.")
                await GStates.start.set()

            else:
                await bot.send_message(callback_query.from_user.id, f'Правильный ответ, {data["step"]} из 5, \n'
                                                                    f'Следующее слово - {data["word"]}',
                                       reply_markup=inline_keyboard)
        elif answer != data.get(answer):
            await bot.send_message(callback_query.from_user.id, f"Неверно.",
                    reply_markup=inline_keyboard)





#.................TRAIN 10 WORDS...................

@dp.message_handler(commands='train_ten', state='*')
async def train_ten(message: types.Message, state: FSMContext):
    await Hstates.random_ten.set()
    res = await get_random()
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = res.get('gender')
        data['word'] = res.get('word')

        await message.reply(f"{data['step']} из 10, Слово - {data['word']}", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda x: x.data in ['Male', 'Female', 'Med'], state=Hstates.random_ten)
async def button_on_click_train_ten(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data['answer']:
            res = await get_random()
            data['step'] += 1
            data['answer'] = res.get('gender')
            data['word'] = res.get('word')

            if data['step'] > 10:
                await bot.send_message(callback_query.from_user.id, "Все ответы верные.")
                await Hstates.start.set()

            else:
                await bot.send_message(callback_query.from_user.id, f'Правильный ответ, {data["step"]} из 10, \n'
                                                                    f'Следующее слово - {data["word"]}',
                                       reply_markup=inline_keyboard)
        elif answer != data.get(answer):
            await bot.send_message(callback_query.from_user.id, f"Неверно.",
                    reply_markup=inline_keyboard)
