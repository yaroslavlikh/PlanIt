from telebot import types


def load_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, "Привет! Я бот лол кек\nЕсли хочешь добавить задачу, то вызови /new\n" \
        "Если хочешь изменить задачу, то вызови /update\n" \
        "Удалить - /delete\n" \
        "Просмотреть список задач - /tasks")