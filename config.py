import os

from dotenv import load_dotenv

def get_token():
    try:
        load_dotenv()
        token = os.getenv("BOT_TOKEN")
        #print(token)
        if token is None:
            print("Токен бота не удалось обнаружить, проверьте, что вы указали его в .env и запускаете main.py из корневой папки")
            raise Exception
        else:
            BOT_TOKEN = token
            return BOT_TOKEN
    except Exception as e:
        print(f"Ошибка при подгрузке токена бота: {e}")