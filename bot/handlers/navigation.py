"""Главное меню, переходы между разделами."""

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from bot.keyboards.menu import get_main_menu, get_back_button
from utils.logger import logger

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start."""
    await message.answer(
        "👋 Добро пожаловать в PlanIt Bot!\n\n"
        "Я помогу вам планировать задачи простым языком.\n"
        "Просто напишите или скажите задачу, и я её структурирую.",
        reply_markup=get_main_menu()
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Обработчик команды /help."""
    await message.answer(
        "ℹ️ <b>Помощь</b>\n\n"
        "📝 <b>Создание задачи:</b>\n"
        "• Нажмите 'Создать задачу'\n"
        "• Выберите способ ввода (текст или голос)\n"
        "• Опишите задачу естественным языком\n"
        "• Подтвердите и выберите, куда сохранить\n\n"
        "📋 <b>Управление задачами:</b>\n"
        "• Просмотр всех задач\n"
        "• Редактирование и удаление\n"
        "• Отправка в интеграции\n\n"
        "🔗 <b>Интеграции:</b>\n"
        "• Google Calendar\n"
        "• Todoist\n"
        "• Yandex Calendar",
        reply_markup=get_back_button(),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "main_menu")
async def callback_main_menu(callback: CallbackQuery):
    """Возврат в главное меню."""
    await callback.message.edit_text(
        "🏠 <b>Главное меню</b>\n\n"
        "Выберите действие:",
        reply_markup=get_main_menu(),
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(F.data == "help")
async def callback_help(callback: CallbackQuery):
    """Помощь через callback."""
    await callback.message.edit_text(
        "ℹ️ <b>Помощь</b>\n\n"
        "📝 <b>Создание задачи:</b>\n"
        "• Нажмите 'Создать задачу'\n"
        "• Выберите способ ввода (текст или голос)\n"
        "• Опишите задачу естественным языком\n"
        "• Подтвердите и выберите, куда сохранить\n\n"
        "📋 <b>Управление задачами:</b>\n"
        "• Просмотр всех задач\n"
        "• Редактирование и удаление\n"
        "• Отправка в интеграции\n\n"
        "🔗 <b>Интеграции:</b>\n"
        "• Google Calendar\n"
        "• Todoist\n"
        "• Yandex Calendar",
        reply_markup=get_back_button(),
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(F.data == "cancel")
async def callback_cancel(callback: CallbackQuery):
    """Отмена операции."""
    await callback.message.edit_text(
        "❌ Операция отменена.",
        reply_markup=get_main_menu()
    )
    await callback.answer("Отменено")
