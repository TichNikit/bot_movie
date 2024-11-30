import html
from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import InputFile
from aiogram.fsm.context import FSMContext
from aiogram.types import InputFile


import requests
from bs4 import BeautifulSoup
import random

from user.bot_answer import (for_start, america_plot_, america_feedback_, america_actors_,
                             club_feedback_, club_actors_, club_plot_,
                             sky_plot_, sky_feedback_, sky_actors_,
                             dream_plot_, dream_feedback_, dream_actors_,
                             just)
from keyboards.kb import (keyboard_start, keyboard_film, keyboard_game, old_films,
                          old_films_1, old_films_2, old_films_3, old_films_4)

# from states.states import User


async def start_command(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, {for_start}',
                         reply_markup=keyboard_start)


async def get_film(message: types.Message):
    await message.answer('Я могу рассказать тебе о своих любимых фильмах или посоветовать фильм на вечер',
                         reply_markup=keyboard_film)

async def get_old_film(message: types.Message):
    await message.answer('Мои любимые фильмы 20 века', reply_markup=old_films)

async def get_game(message: types.Message):
    await message.answer('Любишь игры на ПК? У нас много общего', reply_markup=keyboard_game)

#Красота по американске
async def old_films_1_def(callback: types.CallbackQuery):
    await callback.message.answer('Отличный фильм, но что именно вас интересует?',
                                     reply_markup=old_films_1, show_alert=True)
    await callback.answer()
async def old_films_1_def_plot(callback: types.CallbackQuery):
    await callback.message.edit_text(america_plot_, reply_markup=old_films_1, show_alert=True)
async def old_films_1_def_feedback(callback: types.CallbackQuery):
    await callback.message.edit_text(america_feedback_, reply_markup=old_films_1, show_alert=True)
async def old_films_1_def_actors(callback: types.CallbackQuery):
    await callback.message.edit_text(america_actors_, reply_markup=old_films_1, show_alert=True)

#Бойцовский клуб
async def old_films_2_def(callback: types.CallbackQuery):
    await callback.message.answer('Отличный фильм, но что именно вас интересует?',
                                     reply_markup=old_films_2, show_alert=True)
    await callback.answer()
async def old_films_2_def_plot(callback: types.CallbackQuery):
    await callback.message.edit_text(club_plot_, reply_markup=old_films_2, show_alert=True)
async def old_films_2_def_feedback(callback: types.CallbackQuery):
    await callback.message.edit_text(club_feedback_, reply_markup=old_films_2, show_alert=True)
async def old_films_2_def_actors(callback: types.CallbackQuery):
    await callback.message.edit_text(club_actors_, reply_markup=old_films_2, show_alert=True)

#Достучаться до небес
async def old_films_3_def(callback: types.CallbackQuery):
    await callback.message.answer('Отличный фильм, но что именно вас интересует?',
                                     reply_markup=old_films_3, show_alert=True)
    await callback.answer()
async def old_films_3_def_plot(callback: types.CallbackQuery):
    await callback.message.edit_text(sky_plot_, reply_markup=old_films_3, show_alert=True)
async def old_films_3_def_feedback(callback: types.CallbackQuery):
    await callback.message.edit_text(sky_feedback_, reply_markup=old_films_3, show_alert=True)
async def old_films_3_def_actors(callback: types.CallbackQuery):
    await callback.message.edit_text(sky_actors_, reply_markup=old_films_3, show_alert=True)

#Куда приводят мечты
async def old_films_4_def(callback: types.CallbackQuery):
    await callback.message.answer('Отличный фильм, но что именно вас интересует?',
                                     reply_markup=old_films_4, show_alert=True)
    await callback.answer()
async def old_films_4_def_plot(callback: types.CallbackQuery):
    await callback.message.edit_text(dream_plot_, reply_markup=old_films_4, show_alert=True)
async def old_films_4_def_feedback(callback: types.CallbackQuery):
    await callback.message.edit_text(dream_feedback_, reply_markup=old_films_4, show_alert=True)
async def old_films_4_def_actors(callback: types.CallbackQuery):
    await callback.message.edit_text(dream_actors_, reply_markup=old_films_4, show_alert=True)
#подбор фильма на вечер

async def films(message: types.Message):
    await message.answer('Сейчас что-нибудь подберём...')
    try:
        url = "https://rutube.ru/feeds/movies/"
        response = requests.get(url)
        data = BeautifulSoup(response.text, "html.parser")

        film_data_list = data.find_all('a', class_='wdp-link-module__link wdp-card-poster-module__posterWrapper')

        title_list = []
        film_list = []

        for film_data in film_data_list:
            film_list.append('https://rutube.ru' + film_data['href'])

        title_data_list = data.find_all('div', class_='wdp-card-poster-module__imageWrapper')
        for title_data in title_data_list:
            film_titel = title_data.find('img')
            title_list.append(film_titel['alt'])

        total = random.randint(1, len(title_list))
        film = title_list[total]
        film_url = film_list[total]
        await message.answer(f'Советую вам фильм "{title_list[total]}", который можно посмотреть по ссылки: {film_list[total]}',
                             reply_markup=keyboard_start)
    except Exception:
        await message.answer('Что-то я задумался... О чём мы? (попробуйте повторить попытку)')


async def games(message: types.Message):
    await message.answer('Дайте подумать...')
    try:
        url_game = "https://kanobu.ru/games/popular/?page=2"
        response_game = requests.get(url_game)
        data_game = BeautifulSoup(response_game.text, "html.parser")

        games = data_game.find_all('div', class_='BaseElementCard_body__lXslf')

        game_title_list = []
        game_list = []

        for game in games:
            game_a = game.find('a')
            game_list.append('https://kanobu.ru' + game_a['href'])
            total = str(game_a).find('>') + 1
            game_title_list.append(str(game_a)[total:-4])

        total = random.randint(1, len(game_list))
        await message.answer(f'Могу посоветовать вам игру "{game_title_list[total]}".\n'
                             f'Более подробную информацию об игре можно прочесть по ссылке:{game_list[total]}',
                             reply_markup=keyboard_start)
    except Exception:
        await message.answer('Что-то я задумался... О чём мы? (попробуйте повторить попытку)')


async def games_my(message: types.Message):
    await message.answer('Я немного слукавил, у меня слишком много любимых игр, чтобы выделить какие-то конкретные,'
                         'но может когда-нибудь я всё-таки расскажу о них ;)', reply_markup=keyboard_game)



async def just_answer(message: types.Message):
    total = random.randint(1, len(just))
    await message.answer(just[total], reply_markup=keyboard_start)


def register_user_messages(dp: Dispatcher):
    dp.message.register(start_command, CommandStart())
    dp.message.register(get_film, F.text == 'Фильмы')
    dp.message.register(get_old_film, F.text == 'Мои любимые фильмы')
    dp.message.register(films, F.text == 'Фильм на этот вечер')
    #Красота по американски
    dp.callback_query.register(old_films_1_def, F.data == 'America')
    dp.callback_query.register(old_films_1_def_plot, F.data == 'america_plot')
    dp.callback_query.register(old_films_1_def_feedback, F.data == 'america_feedback')
    dp.callback_query.register(old_films_1_def_actors, F.data == 'america_actors')
    #Бойцовский клуб
    dp.callback_query.register(old_films_2_def, F.data == 'club')
    dp.callback_query.register(old_films_2_def_plot, F.data == 'club_plot')
    dp.callback_query.register(old_films_2_def_feedback, F.data == 'club_feedback')
    dp.callback_query.register(old_films_2_def_actors, F.data == 'club_actors')
    #Достучаться до небес
    dp.callback_query.register(old_films_3_def, F.data == 'sky')
    dp.callback_query.register(old_films_3_def_plot, F.data == 'sky_plot')
    dp.callback_query.register(old_films_3_def_feedback, F.data == 'sky_feedback')
    dp.callback_query.register(old_films_3_def_actors, F.data == 'sky_actors')
    # Куда приводят мечты
    dp.callback_query.register(old_films_4_def, F.data == 'dream')
    dp.callback_query.register(old_films_4_def_plot, F.data == 'dream_plot')
    dp.callback_query.register(old_films_4_def_feedback, F.data == 'dream_feedback')
    dp.callback_query.register(old_films_4_def_actors, F.data == 'dream_actors')
    #остальные ответы
    dp.message.register(just_answer)