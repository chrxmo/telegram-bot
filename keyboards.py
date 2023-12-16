from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start_keyboard = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='/restaurant'),
            KeyboardButton(text='/hotels'),
            KeyboardButton(text='/active_chill'),
            KeyboardButton(text='/passive_chill')
        ],
        [
            KeyboardButton(text='/help')
        ]
    ],resize_keyboard=True,
    one_time_keyboard=True
)


restaurant_keyboard = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Сербская'),
            KeyboardButton(text='Европейская'),
            KeyboardButton(text='Домашняя'),
            KeyboardButton(text='Итальянская')
        ],
        [    KeyboardButton(text='Японская'),
            KeyboardButton(text='Грузинская'),
            KeyboardButton(text='Средиземноморская'),
            KeyboardButton(text='Общая')
        ],
        [
            KeyboardButton(text='Армянская'),
            KeyboardButton(text='Адыгейская'),
            KeyboardButton(text='Кавказская'),
            KeyboardButton(text='Мексиканская')
        ],
        [
            KeyboardButton(text='Украинская'),
            KeyboardButton(text='Американская'),
            KeyboardButton(text='Испанская'),
            KeyboardButton(text='Греческая')
        ],
        [

            KeyboardButton(text='Чешская'),
            KeyboardButton(text='Узбекская'),
            KeyboardButton(text='Паназиатская')
        ],
        [
            KeyboardButton(text='Авторская'),
            KeyboardButton(text='Восточная'),
            KeyboardButton(text='Арабская')
        ]
    ], resize_keyboard=True,
    one_time_keyboard=True
)



active_chill_keyboard = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Компьютерный клуб'),
            KeyboardButton(text='Клуб виртуальной реальности'),
        ],
        [
            KeyboardButton(text='Тир'),
            KeyboardButton(text='Картинг'),
            KeyboardButton(text='Каток'),
            KeyboardButton(text='Скейпарк')
        ],
        [
            KeyboardButton(text='Зоопарк'),
            KeyboardButton(text='Лыжная база'),
            KeyboardButton(text='Верёвочный парк'),
            KeyboardButton(text='Батутный церк')
        ],
        [
            KeyboardButton(text='Страйкбол'),
            KeyboardButton(text='Развлекательный центр'),
            KeyboardButton(text='Полёт на воздушном шаре'),
            KeyboardButton(text='Дайвинг')
        ]
    ], resize_keyboard=True,
    one_time_keyboard=True
)


passive_chill_keyboard = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='Кино'),
            KeyboardButton(text='Парк'),
            KeyboardButton(text='Библиотека')
        ],
        [
            KeyboardButton(text='Театр'),
            KeyboardButton(text='Музей'),
            KeyboardButton(text='Цирк')
        ]
    ], resize_keyboard=True,
    one_time_keyboard=True
)