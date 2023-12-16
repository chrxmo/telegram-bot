from aiogram import types, Bot, Dispatcher, F
from config import bot_token
import asyncio
import logging
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states import Place
from keyboards import restaurant_keyboard, active_chill_keyboard, passive_chill_keyboard, start_keyboard


from weather import lat, lon, open_weather_token, weather

import pandas as pd




bot = Bot(token = bot_token)
dp = Dispatcher()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


async def logs():
    logging.basicConfig(level = logging.INFO)
    await dp.start_polling(bot)



@dp.message(Command('weather'))
async def get_weather(message: types.Message):

    await message.answer(f'{weather(lat, lon, open_weather_token)}')



@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Здравствуйте, расскажите, куда бы вы хотели попасть?\nЧтобы увидеть список команд, используйте /help', reply_markup=start_keyboard)



@dp.message(Command('help'))
async def help(message: types.Message):
    await message.answer('Конечно! Вот список команд:\n/restaurants - если вы хотите посетить ресторан;\n/hotels - если вы хотите посетить отель;\n'
                              '/active_chill - если вы хотите посетить место для активного отдыха;\npassive_chill - если вы хотите посетить место для пассивного отдыха;\n'
                              '/help - если вам снова понадобится помощь.' )



@dp.message(Command('restaurants'))
async def restaurants(message: types.Message, state: FSMContext):

    await state.set_state(Place.restaurant)


    await message.answer('Расскажите, какую кухню вы хотите попробовать?', reply_markup=restaurant_keyboard)



@dp.message(Place.restaurant)
async def find_restaurant(message: types.Message, state: FSMContext):

    file = pd.read_excel('restaurants.xlsx')

    filtered_kitchen_file = file[file['Кухня:'].str.contains(message.text, case=False)]
    filtered_kitchen_file = filtered_kitchen_file[["Название:", "Кухня:", 'Средний чек:']]


    if filtered_kitchen_file.empty:
        await message.answer('Ничего не найдено.')
    else:
        await message.answer(f'Конечно, вот список ресторанов с указанной кухней:\n{filtered_kitchen_file}')

    await state.clear()



@dp.message (Command("hotels"))
async def filter_hotels(message: types.Message, state: FSMContext):
    await state.set_state(Place.hotel)
    await message.answer("Укажите желаемое количество звёзд и цену за одну ночь через запятую (например, '4, 3000').")


@dp.message(Place.hotel)
async def find_hotel(message: types.Message, state: FSMContext):

    stars, avg_check = message.text.split(',')
    stars = int(stars)
    avg_check = int(avg_check)
    file = pd.read_excel('hotels.xlsx')

    filtered_hotels = file[(file['Звёзды'] == stars) & (file['Стоимость за ночь'].between(avg_check - 100000, avg_check + 1000))]
    filtered_hotels = filtered_hotels[['Название', 'Стоимость за ночь', 'Звёзды']]

    if filtered_hotels.empty:
        await message.answer('К сожалению, подходящих отелей не найдено или получен неверный запрос.')
    else:
        await message.answer(f'Вот список подходящих отелей:\n{filtered_hotels}')

    await state.clear()


@dp.message(Command('active_chill'))
async def which_active_chill(message: types.Message, state: FSMContext):

    await state.set_state(Place.active_chill)
    await message.answer('Расскажите подробнее, что бы вы хотели.', reply_markup=active_chill_keyboard)


@dp.message(Place.active_chill)
async def find_active_chill(message: types.Message, state: FSMContext):

    file = pd.read_excel('active_chill.xlsx')
    filtered_active_chill = file[file['Деятельность'].str.contains(message.text, case=False)]
    filtered_active_chill = filtered_active_chill[['Название', 'Рейтинг']]

    if filtered_active_chill.empty:
        await message.answer('К сожалению, ничего не найдено или получен неверный запрос')
    else:
        await message.answer(f'Вот список подходящих вам вариантов:\n{filtered_active_chill}')

    await state.clear()




@dp.message(Command('passive_chill'))
async def which_passive_chill(message: types.Message, state: FSMContext):

    await state.set_state(Place.passive_chill)
    await message.answer('Расскажите подробнее, что бы вы хотели', reply_markup=passive_chill_keyboard)



@dp.message(Place.passive_chill)
async def find_passive_chill(message: types.Message, state: FSMContext):

    file = pd.read_excel('passive_chill.xlsx')
    filtered_passive_chill = file[file['Деятельность:'].str.contains(message.text, case=False)]
    filtered_passive_chill = filtered_passive_chill[['Название:', 'Рейтинг:']]

    if filtered_passive_chill.empty:
        await message.answer('К сожалению, ничего не найдено или получен неверный запрос')
    else:
        await message.answer(f'Вот список подходящих вам вариантов:\n{filtered_passive_chill}')
    await state.clear()





if __name__ == '__main__':
    asyncio.run(logs())