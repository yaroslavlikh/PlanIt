"""Кнопки 'Текстом / Голосом'."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_task_input_methods() -> InlineKeyboardMarkup:
    """Выбор способа ввода задачи."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✍️ Текстом", callback_data="input_text"),
            InlineKeyboardButton(text="🎤 Голосом", callback_data="input_voice")
        ],
        [
            InlineKeyboardButton(text="◀️ Назад", callback_data="main_menu")
        ]
    ])
    return keyboard


def get_cancel_button() -> InlineKeyboardMarkup:
    """Кнопка отмены."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")
        ]
    ])
    return keyboard
