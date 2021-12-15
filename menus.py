from telegram import ReplyKeyboardMarkup, KeyboardButton


faculty_menu = ReplyKeyboardMarkup([
    ['TTF', 'KIF']
], resize_keyboard=True)


courses_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton(text='1-kurs'),
        KeyboardButton(text='2-kurs')
    ],
    [
        KeyboardButton(text='3-kurs'),
        KeyboardButton(text='4-kurs'),
    ],
    [
        KeyboardButton(text='🔙Orqaga'),
        KeyboardButton(text='🔝Asosiy Menyu'),
    ]
], resize_keyboard=True)

tt_menu_1 = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="931-21 TT (o'z)"),
        KeyboardButton(text="932-21 TT (ru)")
    ],
    [
        KeyboardButton(text="941-21 DI (o'z)"),
        KeyboardButton(text="942-21 DI (o'z)")
    ],
    [
        KeyboardButton(text='🔙Orqaga'),
        KeyboardButton(text='🔝Asosiy Menyu'),
    ]
], resize_keyboard=True)

tt_menu_2 = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="931-20 TT (o'z)"),
        KeyboardButton(text="941-20 DI (o'z)")
    ],
    [
        KeyboardButton(text="942-20 DI (o'z)"),
        KeyboardButton(text="943-20 DI (ru)")
    ],
    [
        KeyboardButton(text="932-20 TT (ru)"),
    ],
    [
        KeyboardButton(text='🔙Orqaga'),
        KeyboardButton(text='🔝Asosiy Menyu'),
    ]
], resize_keyboard=True)

tt_menu_3 = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="941-19 DI (o'z)"),
        KeyboardButton(text="942-19 DI (o'z)")
    ],
    [
        KeyboardButton(text="943-19 DI (o'z)"),
        KeyboardButton(text="931-19 TT (o'z)")
    ],
    [
        KeyboardButton(text="932-19 TT (o'z)"),
        KeyboardButton(text="933-19 TT (ru)")
    ],
    [
        KeyboardButton(text="944-19 DI (ru)"),
    ],
    [
        KeyboardButton(text='🔙Orqaga'),
        KeyboardButton(text='🔝Asosiy Menyu'),
    ]
], resize_keyboard=True)

tt_menu_4 = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="941-18 DI (o'z)"),
        KeyboardButton(text="942-18 DI (o'z)")
    ],
    [
        KeyboardButton(text="943-18 DI (o'z)"),
        KeyboardButton(text="931-18 TT (o'z)")
    ],
    [
        KeyboardButton(text="932-18 TT (o'z)"),
        KeyboardButton(text="944-18 DI (ru)")
    ],
    [
        KeyboardButton(text="933-18 TT (ru)"),
    ],
    [
        KeyboardButton(text='🔙Orqaga'),
        KeyboardButton(text='🔝Asosiy Menyu'),
    ]
],resize_keyboard=True)

ki_menu_1 = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="911-21 KI (o'z)"),
        KeyboardButton(text="912-21 KI (o'z)")
    ],
    [
        KeyboardButton(text="913-21 KI (o'z)"),
        KeyboardButton(text="914-21 KI (o'z)")
    ],
    [
        KeyboardButton(text="921-21 AKT (o'z)"),
        KeyboardButton(text="951-21 AX (o'z)")
    ],
    [
        KeyboardButton(text="915-21 KI (ru)"),
        KeyboardButton(text="922-21 AKT (ru)")
    ],
    [
        KeyboardButton(text='🔙Orqaga'),
        KeyboardButton(text='🔝Asosiy Menyu')
    ]
], resize_keyboard=True)

ki_menu_2 = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="911-20 KI (o'z)"),
        KeyboardButton(text="913-20 AT-S (o'z)")
    ],
    [
        KeyboardButton(text="951-20 AX (o'z)"),
        KeyboardButton(text="921-20 AKT (o'z)")
    ],
    [
        KeyboardButton(text="912-20 KI (ru)")
    ],
    [
        KeyboardButton(text='🔙Orqaga'),
        KeyboardButton(text='🔝Asosiy Menyu'),
    ]
], resize_keyboard=True)

ki_menu_3 = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="911-19 KI (o'z)"),
        KeyboardButton(text="912-19 KI (o'z)")
    ],
    [
        KeyboardButton(text="914-19 KI (o'z)"),
        KeyboardButton(text="951-19 AX (o'z)")
    ],
    [
        KeyboardButton(text="921-19 AKT (o'z)"),
        KeyboardButton(text="913-19 KI (ru)")
    ],
    [
        KeyboardButton(text="915-19 KI (ru)"),
        KeyboardButton(text="952-19 AX (ru)")
    ],
    [
        KeyboardButton(text="922-19 AKT (ru)"),
    ],
    [
        KeyboardButton(text='🔙Orqaga'),
        KeyboardButton(text='🔝Asosiy Menyu'),
    ]
], resize_keyboard=True)

def courses(bot, update):
    query = update.callback_query
    reply_markup = KeyboardButtoon(get_main_menu())
    bot.edit_message_text("Example example 2", chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)

    return courses_menu
ki_menu_4 = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="911-18 KI (o'z)"),
        KeyboardButton(text="912-18 KI (o'z)"),
    ],
    [
        KeyboardButton(text="914-18 KI (o'z)"),
        KeyboardButton(text="916-18 KI (o'z)"),
    ],
    [
        KeyboardButton(text="951-18 AX (o'z)"),
        KeyboardButton(text="921-18 AKT (o'z)"),
    ],
    [
        KeyboardButton(text="913-18 KI (ru)"),
        KeyboardButton(text="915-18 KI (ru)"),
    ],
    [
        KeyboardButton(text="952-18 AX (ru)"),
        KeyboardButton(text="922-18 AKT (ru)"),
    ],
    [
        KeyboardButton(text='🔙Orqaga'),
        KeyboardButton(text='🔝Asosiy Menyu'),

    ]
], resize_keyboard=True)