from telebot import types

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
def new_task_markup():
    keyboard = types.InlineKeyboardMarkup() 
    button1 = types.InlineKeyboardButton("Календарь", callback_data="calendar")
    button2 = types.InlineKeyboardButton("Задачи", callback_data="tasks")
    button3 = types.InlineKeyboardButton("Изменить данные", callback_data="edit_task")
    keyboard.add(button1, button2, button3)
    return keyboard

new_task_keyboard = new_task_markup()