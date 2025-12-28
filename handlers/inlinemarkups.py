from telebot import types

####################### стартовый инлайн сука меня заебало их создавать
def start_markup():
    keyboard = types.InlineKeyboardMarkup() 
    button1 = types.InlineKeyboardButton("Начать", callback_data="start")
    keyboard.add(button1)
    return keyboard

start_keyboard = start_markup()

####################### создаем главную инлайн клаву в боте
def main_markup():
    keyboard = types.InlineKeyboardMarkup() 
    button1 = types.InlineKeyboardButton("Календарь", callback_data="calendar")
    button2 = types.InlineKeyboardButton("Новая задача", callback_data="new_task")
    button3 = types.InlineKeyboardButton("Задачи", callback_data="tasks")
    keyboard.add(button1, button2, button3)
    return keyboard

main_keyboard = main_markup()

####################### инлайн клава после добавления новой задачи
def agree_task_markup():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Ок", callback_data="okey")
    button2 = types.InlineKeyboardButton("Изменить", callback_data="change")
    keyboard.add(button1, button2)
    return keyboard

agree_task_keyboard = agree_task_markup()

def new_task_markup():
    keyboard = types.InlineKeyboardMarkup() 
    button1 = types.InlineKeyboardButton("Календарь", callback_data="calendar")
    button2 = types.InlineKeyboardButton("Задачи", callback_data="tasks")
    button3 = types.InlineKeyboardButton("Главное меню", callback_data="start")
    keyboard.add(button1, button2, button3)
    return keyboard

new_task_keyboard = new_task_markup()

####################### инлайн клава после вывода всех задач/расписания
def all_tasks_markup(type_of):
    keyboard = types.InlineKeyboardMarkup()
    if type_of == "task":
        button1 = types.InlineKeyboardButton("Календарь", callback_data="calendar")
    else:
        button1 = types.InlineKeyboardButton("Мои задачи", callback_data="tasks")
    button2 = types.InlineKeyboardButton("Новая задача", callback_data="new_task")
    button3 = types.InlineKeyboardButton("Удалить задачу", callback_data="delete_task")
    keyboard.add(button1, button2, button3)
    return keyboard