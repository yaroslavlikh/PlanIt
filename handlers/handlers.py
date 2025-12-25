from telebot import types
import sqlite3
from api.llm import ask_qwen

def load_handlers(bot):
    ####################### создаем главную инлайн клаву в боте
    main_keyboard = types.InlineKeyboardMarkup() 
    button1 = types.InlineKeyboardButton("Все задачи", callback_data="all_tasks")
    button2 = types.InlineKeyboardButton("Новая задача", callback_data="new_task")
    main_keyboard.add(button1, button2)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Пошел нахуй броук на бедном",
        reply_markup=main_keyboard)

    ###################################### добавление новой задачи
    @bot.callback_query_handler(func=lambda call: call.data == "new_task")
    def add_name_new_task(call):
        print("Перешел в создание новой задачи")
        bot.send_message(call.message.chat.id, "Введите всю информацию про задачу в свободной форме")
        bot.register_next_step_handler(call.message, add_new_task)
    
    def add_new_task(message):
        print("Отправляем запрос LLM")
        info = ask_qwen(message.text.strip())
        info = [el.strip("}").strip("{") for el in info.split(", ")]
        title = info[0]
        start_time = info[1]
        end_time = info[2]
        description = info[3]
        conn = sqlite3.connect('tasks.sql')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tasks (user_id, title, start_time, end_time, description) VALUES (?, ?, ?, ?, ?);',
            (message.chat.id, title, start_time, end_time, description)
        )
        conn.commit()
        cursor.close()
        conn.close()
        bot.send_message(message.chat.id, "Услышал родной, иди нахуй", reply_markup=main_keyboard)

    ##################################### просмотр всех задач 
    @bot.callback_query_handler(func=lambda call: call.data == "all_tasks")
    def get_all_tasks(call):
        print("Выводим все задачи")
        conn = sqlite3.connect('tasks.sql')
        cursor = conn.cursor()
        #cursor.execute(f'SELECT * FROM tasks WHERE user_id = {call.message.chat.id};')
        cursor.execute(f'SELECT * FROM tasks;')
        tasks = cursor.fetchall()
        print(tasks)
        cursor.close()
        conn.close()
        res = ''
        for el in tasks:
            res += f'Название: {el[2]}, дата: {el[3]}\n'
        bot.send_message(call.message.chat.id, f"Вот все твои задачи:\n {res}")