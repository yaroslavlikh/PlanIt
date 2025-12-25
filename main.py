import telebot
from config import get_token
from handlers.handlers import load_handlers
from db import init_db

def start_app(token):
    init_db()
    bot = telebot.TeleBot(token=token)
    load_handlers(bot)
    print("Бот запустился...")
    bot.polling()


if __name__ == '__main__':
    token = get_token()
    start_app(token)