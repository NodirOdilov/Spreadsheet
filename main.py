import logging

from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from config import BOT_TOKEN

from menus import faculty_menu, courses_menu, ki_menu_1, tt_menu_1, ki_menu_2, ki_menu_3, ki_menu_4, tt_menu_4, \
    tt_menu_3, tt_menu_2

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def action(update, context):
    context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)


ADMIN = '590924106'
admin_states = {}
groups_array = {
    '911-21': "Dushanba - Понедельник1️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Dasturlash1 (tajriba)\nO'qituvchi:  ass. Masharipov S./ ass. Bazarboyev M\nXona raqami: 114/108\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Hisob (amaliyot)\nO'qituvchi:  dots.Mamedov Q\nXona raqami: 313\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Xorijiy til1 (amaliyot) \nO'qituvchi:  ass. Adambayeva F./ ass.Sapayeva F. \nXona raqami: 201/219\n\n\n"
              "Seshanba - Вторник2️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: O'zbekiston tarixi (ma'ruza)\nO'qituvchi:  ass. ass. Axmedov G'.\nXona raqami: 212\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: O'zbekiston tarixi (seminar)\nO'qituvchi:  ass. Axmedov G'.\nXona raqami: 216\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Akademik yozuv1 (amaliyot) \nO'qituvchi:  kat.o'qt Matyazova N./ ass.Sapayeva F. \nXona raqami: 313\n\n\n"
              "Chorshanba - Среда3️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Jismoniy tarbiya\nO'qituvchi:  ass. To'liyeva Z.\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Dasturlash1 (ma'ruza)\nO'qituvchi:  dots.Yusupov F.\nXona raqami: 214\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Xorijiy til1(amaliyot) \nO'qituvchi:  ass. Adambayeva F./ ass.Sapayeva F. \nXona raqami: 201/219\n\n\n"
              "Payshanba - Четверг4️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Fizika1 (ma'ruza)\nO'qituvchi:   kat.o'qt.Bobojonov K.\nXona raqami: 214\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Dasturlash1 (tajriba)\nO'qituvchi:  ass. Masharipov S./ ass. Bazarboyev M.\nXona raqami: 114/107\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Fizika1 (amaliyot) \nO'qituvchi:  ass. Rajabov A. \nXona raqami: 215a\n\n\n"
              "Juma - Пятница5️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Hisob (ma'ruza)\nO'qituvchi: dots.Mamedov Q.\nXona raqami: 214\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Hisob (amaliyot)\nO'qituvchi:   dots.Mamedov Q.\nXona raqami: 311\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Murabbiylik soati \nO'qituvchi: ass.Ishmetov B. \nXona raqami: 308\n\n\n"
              "Shanba - Суббота6️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Hisob (ma'ruza)\nO'qituvchi: dots.Mamedov Q.\nXona raqami: 214\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Fizika1 (tajriba)\nO'qituvchi: kat.o'qt.Bobojonov K./ ass. Rajabov A.\nXona raqami: 215a/217",
    '912-21': "Dushanba - Понедельник1️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Hisob (amaliyot)\nO'qituvchi: dots.Mamedov Q.\nXona raqami: 118\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Dasturlash1 (tajriba)\nO'qituvchi: ass. Masharipov S./ ass. Bazarboyev M.\nXona raqami: 114/108\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Fizika1 (amaliyot) \nO'qituvchi: kat.o'qt.Bobojonov K. \nXona raqami: 118\n\n\n"
              "Seshanba - Вторник2️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: O'zbekiston tarixi (ma'ruza)\nO'qituvchi: ass. Axmedov G'.\nXona raqami: 212\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Jismoniy tarbiya\nO'qituvchi: ass. To'liyeva Z.\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Dasturlash1 (tajriba) \nO'qituvchi: ass. Masharipov S./ ass. Bazarboyev M. \nXona raqami: 114/321\n\n\n"
              "Chorshanba - Среда3️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Fizika1 (tajriba) \nO'qituvchi: ass. Rajabov A./ ass. Qadambayeva N.\nXona raqami:215а/118\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Dasturlash1 (ma'ruza)\nO'qituvchi:  dots.Yusupov F.\nXona raqami: 214\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Murabbiylik soati \nO'qituvchi: ass. ass.Ishmetov B. \nXona raqami: 310\n\n\n"
              "Payshanba - Четверг4️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Fizika1 (ma'ruza)\nO'qituvchi:   kat.o'qt.Bobojonov K.\nXona raqami: 214\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Hisob (amaliyot)\nO'qituvchi:  dots.Mamedov Q.\nXona raqami: 118\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Akademik yozuv1 (amaliyot) \nO'qituvchi: kat.o'qt Matyazova N.\nXona raqami: 118\n\n\n",
              "Juma - Пятница5️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Hisob (ma'ruza)\nO'qituvchi: dots.Mamedov Q.\nXona raqami: 214\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Xorijiy til1(amaliyot)\nO'qituvchi: ass. Adambayeva F./ kat.o'qt.Xo'janiyazova G.\nXona raqami: 219/307\n\n\n"
              "Shanba - Суббота6️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Hisob (ma'ruza) \nO'qituvchi: dots.Mamedov Q.\nXona raqami: 214\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: O'zbekiston tarixi (seminar)\nO'qituvchi:  ass. Axmedov G'.\nXona raqami: 118\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Xorijiy til1(amaliyot) \nass. Adambayeva F./ kat.o'qt.Xo'janiyazova G.  \nXona raqami: 118/307\n\n\n"
    '913-21': "Dushanba - Понедельник1️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Xorijiy til1(amaliyot)\nO'qituvchi: kat.o'qt.Xo'janiyazova G./ ass.Sapayeva F.\nXona raqami: 307/201\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Dasturlash1 (tajriba)\nO'qituvchi: ass. Yusupova J./ ass. Allamova Sh.\nXona raqami: 213/109\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: O'zbekiston tarixi (seminar) \nO'qituvchi: ass. Axmedov G' \nXona raqami:  313\n\n\n"
              "Seshanba - Вторник2️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: O'zbekiston tarixi (ma'ruza)\nO'qituvchi: ass. Axmedov G'.\nXona raqami: 212\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Hisob (amaliyot)\nO'qituvchi: dots.Mamedov Q.\nXona raqami: 308\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Jismoniy tarbiya \nO'qituvchi: ass. To'liyeva Z.\n\n\n"
              "Chorshanba - Среда3️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Xorijiy til1(amaliyot) \nO'qituvchi: kat.o'qt.Xo'janiyazova G./ ass.Sapayeva F.\nXona raqami:307/201\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Dasturlash1 (ma'ruza)\nO'qituvchi:  dots.Yusupov F.\nXona raqami: 214\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Akademik yozuv1 (amaliyot)  \nO'qituvchi:  kat.o'qt Matyazova N. \nXona raqami: 217\n\n\n"
              "Payshanba - Четверг4️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Fizika1 (ma'ruza)\nO'qituvchi:   kat.o'qt.Bobojonov K.\nXona raqami: 214\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Fizika1 (tajriba)\nO'qituvchi:  kat.o'qt.Bobojonov K./ ass. Rajabov A.\nXona raqami: 313/215a\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Fizika1 (amaliyot) \nO'qituvchi: kat.o'qt.Bobojonov K.\nXona raqami: 313\n\n\n"
              "Juma - Пятница5️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Hisob (ma'ruza)\nO'qituvchi: dots.Mamedov Q.\nXona raqami: 214\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Murabbiylik soati \nO'qituvchi: ass. ass.Ishmetov B.\nXona raqami:  312\n\n\n"
              "Shanba - Суббота6️⃣\n⏰ 08:30 dan 09:50 gacha:\n📚 Fan nomi: Hisob (ma'ruza) \nO'qituvchi: dots.Mamedov Q.\nXona raqami: 214\n\n⏰ 10:00 dan 11:20 gacha:\n📚 Fan nomi: Dasturlash1 (tajriba)\nO'qituvchi: ass. Yusupova J./ ass. Allamova Sh.\nXona raqami: 213/109\n\n⏰ 11:30 dan 12:50 gacha:\n📚 Fan nomi: Hisob (amaliyot)  \nO'qituvchi: dots.Mamedov Q.  \nXona raqami: 308\n\n\n",

}

user_states = {
    'faculty': 'u1',
    'courses': 'u2',
    'groups': 'u3'
}

# Variables for use in future
admin_steps = []
test_steps = []

def start(update, context):
    chat_id = str(update.message.from_user.id)
    update.message.reply_text("Assalomu aleykum - Здравствуйте\nFakultetni tanlang - Выберите факультет:", reply_markup=faculty_menu)
    return user_states['faculty']


def courses(update, context):
    admin_steps.clear()
    admin_steps.append(update.message.text)
    print(admin_steps)
    update.message.reply_text("Kursni tanlang - Выберите курс:", reply_markup=courses_menu)
    return user_states['courses']

def groups(update, context):
    number = update.message.text[0]
    if admin_steps[0] == 'TT':
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
#
# def  back(update, context):
#

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher


    controller = ConversationHandler(
        entry_points=[
            CommandHandler('start', start)
        ],
        states={
            user_states['faculty']: [
                MessageHandler(Filters.regex("TT"), courses),
                MessageHandler(Filters.regex("KI"), courses)
            ],
            user_states['courses']: [
                MessageHandler(Filters.regex("1-kurs"), groups),
                MessageHandler(Filters.regex("2-kurs"), groups),
                MessageHandler(Filters.regex("3-kurs"), groups),
                MessageHandler(Filters.regex("4-kurs"), groups),
                MessageHandler(Filters.regex("Orqaga"), start),
                MessageHandler(Filters.regex("Asosiy Menyu"), start)
            ],
            user_states['groups']: [
                MessageHandler(Filters.text, salom),
                MessageHandler(Filters.regex("Orqaga"), courses),
                MessageHandler(Filters.regex("Asosiy Menyu"), start)
            ]
        },
        fallbacks=[
            CommandHandler('start', start),
        ]
    )

    dispatcher.add_handler(controller)
    dispatcher.add_handler(MessageHandler(Filters.text, action))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()