from telebot import types
import sqlite3
from api.whisper import new_voice
from api.llm import ask_qwen
from handlers.return_task import ret_cal, ret_task
from handlers.inlinemarkups import (
    main_keyboard, new_task_keyboard, all_tasks_markup, start_keyboard, agree_task_keyboard
)

def load_handlers(bot):
    @bot.message_handler(commands=['start'])
    def starting_bot(message):
        bot.send_message(message.chat.id, "Привет! Let's Plan It!",
        reply_markup=start_keyboard)

    ######################################
    @bot.callback_query_handler(func=lambda call: call.data == "start")
    def start(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Главное меню",
        reply_markup=main_keyboard)

    ###################################### добавление новой задачи
    @bot.callback_query_handler(func=lambda call: call.data == "new_task")
    def add_name_new_task(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        print("Перешел в создание новой задачи")
        bot.send_message(call.message.chat.id, "Введите всю информацию про задачу в свободной форме")
        bot.register_next_step_handler(call.message, add_new_task)
    
    def add_new_task(message):
        if message.content_type == 'voice':
            print("Получено голосовое сообщение")
            info = new_voice(message, bot)
        if message.content_type == 'text':
            info = message.text.strip()
        info = ask_qwen(info)
        info = [el.strip("}").strip("{") for el in info.split("; ")]
        title = info[0]
        start_date = info[1]
        start_time = info[2]
        end_time = info[3]
        description = info[4]
        type_of = info[5]
        conn = sqlite3.connect('tasks.sql')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tasks (user_id, title, start_date, start_time, end_time, description, type) VALUES (?, ?, ?, ?, ?, ?, ?);',
            (message.chat.id, title, start_date, start_time, end_time, description, type_of)
        )
        conn.commit()
        cursor.close()
        conn.close()
        if type_of == "расписание":
            ans = ret_cal(info)
            ans = ', '.join(ans)
        else:
            ans = ret_task(info)
            ans = ', '.join(ans)
        bot.send_message(message.chat.id, f'Добавляем в {type_of}?:\n{ans}', reply_markup=agree_task_keyboard)
        

    ##################################### просмотр расписания
    @bot.callback_query_handler(func=lambda call: call.data == "calendar")
    def get_calendar(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        print("Выводим расписание")
        conn = sqlite3.connect('tasks.sql')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE user_id = ? AND type = ?;",
            (call.message.chat.id, "расписание")
        )
        tasks = cursor.fetchall()
        print(tasks)
        cursor.close()
        conn.close()
        res = ''

        for el in tasks:
            task_parts = ret_cal(el)
            res += ', '.join(task_parts) + '\n'
        
        all_tasks_keyboard = all_tasks_markup("calendar")
        if not tasks or not res.strip():
            bot.send_message(call.message.chat.id, 'У вас пока нет планов', reply_markup=all_tasks_keyboard)
        else:
            bot.send_message(call.message.chat.id, f"Вот все твое расписание:\n {res}", reply_markup=all_tasks_keyboard)

    ##################################### просмотр задач
    @bot.callback_query_handler(func=lambda call: call.data == "tasks")
    def get_all_tasks(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        print("Выводим задачи")
        conn = sqlite3.connect('tasks.sql')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE user_id = ? AND type = ?;",
            (call.message.chat.id, "задача")
        )
        tasks = cursor.fetchall()
        print(tasks)
        cursor.close()
        conn.close()
        res = ''
        for el in tasks:
            task_parts = ret_task(el)
            res += ', '.join(task_parts) + '\n'

        all_tasks_keyboard = all_tasks_markup("tasks")
        if not tasks or not res.strip():
            bot.send_message(call.message.chat.id, "У вас пока нет задач", reply_markup=all_tasks_keyboard)
        else:
            bot.send_message(call.message.chat.id, f"Вот все твое расписание:\n {res}", reply_markup=all_tasks_keyboard)