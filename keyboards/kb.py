from aiogram import types

keyboard_start = [[types.KeyboardButton(text='Фильмы')]]
keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard_start)

keyboard_film = [[types.KeyboardButton(text='Мои любимые фильмы'), types.KeyboardButton(text='Фильм на этот вечер')]]
keyboard_film = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard_film)

keyboard_game = [[types.KeyboardButton(text='Мои любимые игры'), types.KeyboardButton(text='Мои рекомендации')]]
keyboard_game = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard_game)

old_films = [
    [types.InlineKeyboardButton(text="Красота по американске", callback_data='America')],
    [types.InlineKeyboardButton(text="Бойцовский клуб", callback_data='club')],
    [types.InlineKeyboardButton(text="Достучаться до небес", callback_data='sky')],
    [types.InlineKeyboardButton(text="Куда приводят мечты", callback_data='dream')]]
old_films = types.InlineKeyboardMarkup(inline_keyboard=old_films)


old_films_1 = [
    [types.InlineKeyboardButton(text="Сюжет", callback_data='america_plot')],
    [types.InlineKeyboardButton(text="Критика", callback_data='america_feedback')],
    [types.InlineKeyboardButton(text="Главные роли", callback_data='america_actors')]
]
old_films_1 = types.InlineKeyboardMarkup(inline_keyboard=old_films_1)

old_films_2 = [
    [types.InlineKeyboardButton(text="Сюжет", callback_data='club_plot')],
    [types.InlineKeyboardButton(text="Критика", callback_data='club_feedback')],
    [types.InlineKeyboardButton(text="Главные роли", callback_data='club_actors')]
]
old_films_2 = types.InlineKeyboardMarkup(inline_keyboard=old_films_2)

old_films_3 = [
    [types.InlineKeyboardButton(text="Сюжет", callback_data='sky_plot')],
    [types.InlineKeyboardButton(text="Критика", callback_data='sky_feedback')],
    [types.InlineKeyboardButton(text="Главные роли", callback_data='sky_actors')]
]
old_films_3 = types.InlineKeyboardMarkup(inline_keyboard=old_films_3)

old_films_4 = [
    [types.InlineKeyboardButton(text="Сюжет", callback_data='dream_plot')],
    [types.InlineKeyboardButton(text="Критика", callback_data='dream_feedback')],
    [types.InlineKeyboardButton(text="Главные роли", callback_data='dream_actors')]
]
old_films_4 = types.InlineKeyboardMarkup(inline_keyboard=old_films_4)





