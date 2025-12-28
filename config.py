import os

from dotenv import load_dotenv

def get_token_bot():
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

def get_token_gemini():
    try:
        load_dotenv()
        token = os.getenv("GEMINI_API_KEY")
        #print(token)
        if token is None:
            print("Токен gemini не удалось обнаружить, проверьте, что вы указали его в .env и запускаете main.py из корневой папки")
            raise Exception
        else:
            GEMINI_API_KEY = token
            return GEMINI_API_KEY
    except Exception as e:
        print(f"Ошибка при подгрузке токена gemini: {e}")

        