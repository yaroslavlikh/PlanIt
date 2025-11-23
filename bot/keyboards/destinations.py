"""Выбор целей (локально, Google, Todoist...)."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import List


def get_destinations_keyboard(available_integrations: List[str] = None) -> InlineKeyboardMarkup:
    """Клавиатура выбора целей для сохранения задачи."""
    if available_integrations is None:
        available_integrations = []
    
    buttons = []
    
    # Локальное сохранение
    buttons.append([
        InlineKeyboardButton(text="💾 Локально", callback_data="dest_local")
    ])
    
    # Интеграции
    if "google_calendar" in available_integrations:
        buttons.append([
            InlineKeyboardButton(text="📅 Google Calendar", callback_data="dest_google")
        ])
    
    if "todoist" in available_integrations:
        buttons.append([
            InlineKeyboardButton(text="✅ Todoist", callback_data="dest_todoist")
        ])
    
    if "yandex_calendar" in available_integrations:
        buttons.append([
            InlineKeyboardButton(text="📆 Yandex Calendar", callback_data="dest_yandex")
        ])
    
    # Множественный выбор
    buttons.append([
        InlineKeyboardButton(text="📤 В несколько мест", callback_data="dest_multiple")
    ])
    
    # Отмена
    buttons.append([
        InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")
    ])
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_multiple_destinations_keyboard(available_integrations: List[str] = None) -> InlineKeyboardMarkup:
    """Клавиатура множественного выбора целей."""
    if available_integrations is None:
        available_integrations = []
    
    buttons = []
    
    # Чекбоксы для выбора
    row = []
    row.append(InlineKeyboardButton(text="☑️ Локально", callback_data="toggle_local"))
    if len(row) == 2:
        buttons.append(row)
        row = []
    
    if "google_calendar" in available_integrations:
        row.append(InlineKeyboardButton(text="☐ Google Calendar", callback_data="toggle_google"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    
    if "todoist" in available_integrations:
        row.append(InlineKeyboardButton(text="☐ Todoist", callback_data="toggle_todoist"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    
    if row:
        buttons.append(row)
    
    # Подтверждение
    buttons.append([
        InlineKeyboardButton(text="✅ Сохранить", callback_data="save_multiple")
    ])
    
    buttons.append([
        InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_destinations")
    ])
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
