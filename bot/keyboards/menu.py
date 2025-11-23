"""Главное меню, подменю."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu() -> InlineKeyboardMarkup:
    """Главное меню бота."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Создать задачу", callback_data="create_task")
        ],
        [
            InlineKeyboardButton(text="📋 Мои задачи", callback_data="my_tasks")
        ],
        [
            InlineKeyboardButton(text="🔗 Интеграции", callback_data="integrations"),
            InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help")
        ]
    ])
    return keyboard


def get_back_button(callback_data: str = "main_menu") -> InlineKeyboardMarkup:
    """Кнопка 'Назад'."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Назад", callback_data=callback_data)
        ]
    ])
    return keyboard
