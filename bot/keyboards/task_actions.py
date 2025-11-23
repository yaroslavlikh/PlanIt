"""Кнопки у задач: '✏️ Изменить', '🗑 Удалить'."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import Optional


def get_task_actions_keyboard(task_id: int) -> InlineKeyboardMarkup:
    """Клавиатура действий с задачей."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✏️ Изменить", callback_data=f"edit_task_{task_id}"),
            InlineKeyboardButton(text="🗑 Удалить", callback_data=f"delete_task_{task_id}")
        ],
        [
            InlineKeyboardButton(text="📤 Отправить в...", callback_data=f"send_task_{task_id}")
        ],
        [
            InlineKeyboardButton(text="◀️ Назад к списку", callback_data="my_tasks")
        ]
    ])
    return keyboard


def get_tasks_list_keyboard(tasks: list, page: int = 0, per_page: int = 5) -> InlineKeyboardMarkup:
    """Клавиатура списка задач с пагинацией."""
    buttons = []
    
    # Задачи на текущей странице
    start = page * per_page
    end = start + per_page
    page_tasks = tasks[start:end]
    
    for task in page_tasks:
        task_title = task.get("title", "Без названия")[:30]
        task_id = task.get("id")
        buttons.append([
            InlineKeyboardButton(
                text=f"📌 {task_title}",
                callback_data=f"view_task_{task_id}"
            )
        ])
    
    # Пагинация
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text="◀️", callback_data=f"tasks_page_{page-1}"))
    
    if end < len(tasks):
        nav_buttons.append(InlineKeyboardButton(text="▶️", callback_data=f"tasks_page_{page+1}"))
    
    if nav_buttons:
        buttons.append(nav_buttons)
    
    # Назад в меню
    buttons.append([
        InlineKeyboardButton(text="◀️ Главное меню", callback_data="main_menu")
    ])
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_confirm_delete_keyboard(task_id: int) -> InlineKeyboardMarkup:
    """Клавиатура подтверждения удаления."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Да, удалить", callback_data=f"confirm_delete_{task_id}"),
            InlineKeyboardButton(text="❌ Отмена", callback_data=f"view_task_{task_id}")
        ]
    ])
    return keyboard
