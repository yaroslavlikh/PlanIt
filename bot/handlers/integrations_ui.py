"""Управление подключениями (подключить/отключить)."""

from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot.keyboards.menu import get_back_button, get_main_menu
from utils.logger import logger

router = Router()


def get_integrations_keyboard(connected_integrations: list = None) -> InlineKeyboardMarkup:
    """Клавиатура управления интеграциями."""
    if connected_integrations is None:
        connected_integrations = []
    
    buttons = []
    
    # Google Calendar
    is_google_connected = "google_calendar" in connected_integrations
    google_text = "🔗 Google Calendar" if is_google_connected else "📅 Google Calendar"
    google_action = "disconnect_google" if is_google_connected else "connect_google"
    buttons.append([
        InlineKeyboardButton(
            text=f"{google_text} {'✅' if is_google_connected else '❌'}",
            callback_data=google_action
        )
    ])
    
    # Todoist
    is_todoist_connected = "todoist" in connected_integrations
    todoist_text = "🔗 Todoist" if is_todoist_connected else "✅ Todoist"
    todoist_action = "disconnect_todoist" if is_todoist_connected else "connect_todoist"
    buttons.append([
        InlineKeyboardButton(
            text=f"{todoist_text} {'✅' if is_todoist_connected else '❌'}",
            callback_data=todoist_action
        )
    ])
    
    # Yandex Calendar
    is_yandex_connected = "yandex_calendar" in connected_integrations
    yandex_text = "🔗 Yandex Calendar" if is_yandex_connected else "📆 Yandex Calendar"
    yandex_action = "disconnect_yandex" if is_yandex_connected else "connect_yandex"
    buttons.append([
        InlineKeyboardButton(
            text=f"{yandex_text} {'✅' if is_yandex_connected else '❌'}",
            callback_data=yandex_action
        )
    ])
    
    buttons.append([
        InlineKeyboardButton(text="◀️ Назад", callback_data="main_menu")
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@router.callback_query(F.data == "integrations")
async def callback_integrations(callback: CallbackQuery):
    """Показать список интеграций."""
    # Здесь будет запрос к БД для получения подключённых интеграций
    # Пока заглушка
    connected_integrations = []
    
    await callback.message.edit_text(
        "🔗 <b>Интеграции</b>\n\n"
        "Подключите внешние сервисы для синхронизации задач:\n\n"
        "• Google Calendar — синхронизация с календарём\n"
        "• Todoist — управление задачами\n"
        "• Yandex Calendar — календарь Яндекса",
        reply_markup=get_integrations_keyboard(connected_integrations),
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(F.data == "connect_google")
async def callback_connect_google(callback: CallbackQuery):
    """Подключение Google Calendar."""
    await callback.message.edit_text(
        "📅 <b>Подключение Google Calendar</b>\n\n"
        "Функция подключения будет реализована позже.\n"
        "Здесь будет OAuth авторизация.",
        reply_markup=get_back_button("integrations"),
        parse_mode="HTML"
    )
    await callback.answer("Подключение в разработке")


@router.callback_query(F.data == "disconnect_google")
async def callback_disconnect_google(callback: CallbackQuery):
    """Отключение Google Calendar."""
    # Здесь будет отключение из БД
    await callback.message.edit_text(
        "✅ <b>Google Calendar отключён</b>",
        reply_markup=get_integrations_keyboard([])
    )
    await callback.answer("Google Calendar отключён")


@router.callback_query(F.data == "connect_todoist")
async def callback_connect_todoist(callback: CallbackQuery):
    """Подключение Todoist."""
    await callback.message.edit_text(
        "✅ <b>Подключение Todoist</b>\n\n"
        "Введите API токен Todoist:",
        reply_markup=get_back_button("integrations"),
        parse_mode="HTML"
    )
    await callback.answer("Введите токен")


@router.callback_query(F.data == "disconnect_todoist")
async def callback_disconnect_todoist(callback: CallbackQuery):
    """Отключение Todoist."""
    await callback.message.edit_text(
        "✅ <b>Todoist отключён</b>",
        reply_markup=get_integrations_keyboard([])
    )
    await callback.answer("Todoist отключён")


@router.callback_query(F.data == "connect_yandex")
async def callback_connect_yandex(callback: CallbackQuery):
    """Подключение Yandex Calendar."""
    await callback.message.edit_text(
        "📆 <b>Подключение Yandex Calendar</b>\n\n"
        "Функция подключения будет реализована позже.\n"
        "Здесь будет OAuth авторизация.",
        reply_markup=get_back_button("integrations"),
        parse_mode="HTML"
    )
    await callback.answer("Подключение в разработке")


@router.callback_query(F.data == "disconnect_yandex")
async def callback_disconnect_yandex(callback: CallbackQuery):
    """Отключение Yandex Calendar."""
    await callback.message.edit_text(
        "✅ <b>Yandex Calendar отключён</b>",
        reply_markup=get_integrations_keyboard([])
    )
    await callback.answer("Yandex Calendar отключён")
