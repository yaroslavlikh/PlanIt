"""Подтверждение задачи + выбор целей."""

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.keyboards.destinations import get_destinations_keyboard
from bot.keyboards.menu import get_main_menu
from utils.logger import logger
from utils.datetime_helpers import format_datetime

router = Router()


async def show_task_draft(message: Message, state: FSMContext):
    """Показать черновик задачи для подтверждения."""
    data = await state.get_data()
    task_text = data.get("task_text", "")
    
    # Здесь будет вызов Yandex GPT для парсинга
    # Пока заглушка с базовой структурой
    task_data = {
        "title": task_text[:50] + "..." if len(task_text) > 50 else task_text,
        "description": task_text,
        "due_date": None,  # Будет извлечено парсером
        "location": None  # Будет извлечено парсером
    }
    
    # Сохраняем в состояние
    await state.update_data(task_draft=task_data)
    
    # Формируем текст для отображения
    text = f"📋 <b>Черновик задачи:</b>\n\n"
    text += f"<b>Название:</b> {task_data['title']}\n"
    
    if task_data.get('due_date'):
        text += f"<b>Дата:</b> {format_datetime(task_data['due_date'])}\n"
    
    if task_data.get('location'):
        text += f"<b>Место:</b> {task_data['location']}\n"
    
    text += f"\n<b>Описание:</b> {task_data['description']}\n\n"
    text += "Выберите, куда сохранить задачу:"
    
    # Получаем доступные интеграции (пока заглушка)
    available_integrations = []  # Будет из БД
    
    await message.answer(
        text,
        reply_markup=get_destinations_keyboard(available_integrations),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith("dest_"))
async def callback_choose_destination(callback: CallbackQuery, state: FSMContext):
    """Выбор цели для сохранения задачи."""
    destination = callback.data.replace("dest_", "")
    
    data = await state.get_data()
    task_draft = data.get("task_draft", {})
    
    if not task_draft:
        await callback.answer("Ошибка: черновик задачи не найден", show_alert=True)
        return
    
    # Сохраняем задачу
    destinations_map = {
        "local": "Локально",
        "google": "Google Calendar",
        "todoist": "Todoist",
        "yandex": "Yandex Calendar"
    }
    
    dest_name = destinations_map.get(destination, "Неизвестно")
    
    # Здесь будет реальное сохранение
    # Пока заглушка
    await callback.message.edit_text(
        f"✅ <b>Задача сохранена!</b>\n\n"
        f"📌 <b>Название:</b> {task_draft.get('title', 'Без названия')}\n"
        f"📍 <b>Куда:</b> {dest_name}\n\n"
        f"Задача успешно добавлена.",
        reply_markup=get_main_menu(),
        parse_mode="HTML"
    )
    
    await callback.answer(f"Задача сохранена в {dest_name}")
    await state.clear()


@router.callback_query(F.data == "dest_multiple")
async def callback_multiple_destinations(callback: CallbackQuery, state: FSMContext):
    """Выбор нескольких целей."""
    await callback.message.edit_text(
        "📤 <b>Выбор нескольких мест</b>\n\n"
        "Выберите все места, куда нужно сохранить задачу:",
        reply_markup=get_destinations_keyboard(),  # Будет специальная клавиатура
        parse_mode="HTML"
    )
    await callback.answer()
