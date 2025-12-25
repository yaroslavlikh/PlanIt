import telebot
from config import get_token
from handlers.handlers import load_handlers

def start_app(token):
    bot = telebot.TeleBot(token=token)
    load_handlers(bot)
    print("Бот запустился...")
    bot.polling()


if __name__ == '__main__':
    token = get_token()
    start_app(token)