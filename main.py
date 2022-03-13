import json
import logging

from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, PicklePersistence
from config import BOT_TOKEN
from groups import groups_array

from menus import faculty_menu, courses_menu, ki_menu_1, tt_menu_1, ki_menu_2, ki_menu_3, ki_menu_4, tt_menu_4, \
    tt_menu_3, tt_menu_2

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def action(update, context):
    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)




ADMIN = '590924106'

user_states = {
    'faculty': 'u1',
    'courses': 'u2',
    'groups': 'u3'
}

# Variables for use in future
admin_steps = []

def read():
    with open('steps.json') as json_file:
        return json.load(json_file)


def write(text):
    admin_steps.clear()
    admin_steps.append(text)
    with open('steps.json', 'w') as outfile:
        json_string = json.dumps(admin_steps)
        outfile.write(json_string)


def start(update, context):
    chat_id = str(update.message.from_user.id)
    update.message.reply_text("Assalomu aleykum - Здравствуйте\nFakultetni tanlang - Выберите факультет:", reply_markup=faculty_menu)
    return user_states['faculty']


def courses(update, context):
    if update.message.text != "🔙Orqaga":
        # admin_steps.clear()
        # admin_steps.append(update.message.text)
        write(update.message.text)
    # print(admin_steps)
    update.message.reply_text("Kursni tanlang - Выберите курс:", reply_markup=courses_menu)
    return user_states['courses']

def groups(update, context):
    number = update.message.text[0]
    if read()[0] == 'TTF':
        if number == '1':
            m = tt_menu_1
        elif number == '2':
            m = tt_menu_2
        elif number == '3':
            m = tt_menu_3
        else:
            m = tt_menu_4
    else:
        if number == '1':
            m = ki_menu_1
        elif number == '2':
            m = ki_menu_2
        elif number == '3':
            m = ki_menu_3
        else:
            m = ki_menu_4
    update.message.reply_text("Guruhni tanlang - Выберите группу:", reply_markup=m)
    return user_states['groups']


def salom(update, context):
    g_number = update.message.text.split()[0]
    if g_number in groups_array:
        update.message.reply_text(groups_array[g_number])
    return user_states['groups']


def main():
    persistence = PicklePersistence(filename='conversationbot')
    updater = Updater(BOT_TOKEN, persistence=persistence, use_context=True)
    dispatcher = updater.dispatcher


    controller = ConversationHandler(
        entry_points=[
            CommandHandler('start', start)
        ],
        states={
            user_states['faculty']: [
                CommandHandler('start', start),
                MessageHandler(Filters.regex("TTF"), courses),
                MessageHandler(Filters.regex("KIF"), courses)
            ],
            user_states['courses']: [
                CommandHandler('start', start),
                MessageHandler(Filters.regex("1-kurs"), groups),
                MessageHandler(Filters.regex("2-kurs"), groups),
                MessageHandler(Filters.regex("3-kurs"), groups),
                MessageHandler(Filters.regex("4-kurs"), groups),
                MessageHandler(Filters.regex("🔙Orqaga"), start),
                MessageHandler(Filters.regex("🔝Asosiy Menyu"), start)
            ],
            user_states['groups']: [
                CommandHandler('start', start),
                MessageHandler(Filters.regex("🔙Orqaga"), courses),
                MessageHandler(Filters.regex("🔝Asosiy Menyu"), start),
                MessageHandler(Filters.text, salom)
            ]
        },
        fallbacks=[
            CommandHandler('start', start),
        ],
        allow_reentry=True,
        name="my_conversation",
        persistent=True,
    )

    dispatcher.add_handler(controller)
    dispatcher.add_handler(MessageHandler(Filters.text, action))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()