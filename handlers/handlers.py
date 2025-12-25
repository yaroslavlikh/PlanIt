from telebot import types
import sqlite3

def load_handlers(bot):
    main_keyboard = types.InlineKeyboardMarkup() # создаем главную инлайн клаву в боте
    button1 = types.InlineKeyboardButton("Все задачи", callback_data="all_lasks")
    button2 = types.InlineKeyboardButton("Новая задача", callback_data="new_task")
    main_keyboard.add(button1, button2)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Пошел нахуй броук на бедном",
        reply_markup=main_keyboard)

    @bot.message_handler()
    def add_new_task():
        return