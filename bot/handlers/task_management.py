"""Просмотр, редактирование, удаление задач."""

from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot.keyboards.task_actions import (
    get_task_actions_keyboard,
    get_tasks_list_keyboard,
    get_confirm_delete_keyboard
)
from bot.keyboards.menu import get_main_menu
from utils.logger import logger

router = Router()


@router.callback_query(F.data == "my_tasks")
async def callback_my_tasks(callback: CallbackQuery):
    """Показать список задач пользователя."""
    # Здесь будет запрос к БД
    # Пока заглушка
    tasks = [
        {"id": 1, "title": "Пример задачи 1"},
        {"id": 2, "title": "Пример задачи 2"},
    ]
    
    if not tasks:
        await callback.message.edit_text(
            "📋 <b>Мои задачи</b>\n\n"
            "У вас пока нет задач.\n"
            "Создайте первую задачу!",
            reply_markup=get_main_menu(),
            parse_mode="HTML"
        )
    else:
        await callback.message.edit_text(
            f"📋 <b>Мои задачи</b>\n\n"
            f"Найдено задач: {len(tasks)}\n"
            f"Выберите задачу:",
            reply_markup=get_tasks_list_keyboard(tasks),
            parse_mode="HTML"
        )
    
    await callback.answer()


@router.callback_query(F.data.startswith("view_task_"))
async def callback_view_task(callback: CallbackQuery):
    """Просмотр конкретной задачи."""
    task_id = int(callback.data.replace("view_task_", ""))
    
    # Здесь будет запрос к БД
    # Пока заглушка
    task = {
        "id": task_id,
        "title": f"Задача #{task_id}",
        "description": "Описание задачи",
        "due_date": None,
        "location": None
    }
    
    text = f"📌 <b>Задача #{task_id}</b>\n\n"
    text += f"<b>Название:</b> {task['title']}\n"
    
    if task.get('description'):
        text += f"<b>Описание:</b> {task['description']}\n"
    
    if task.get('due_date'):
        from utils.datetime_helpers import format_datetime
        text += f"<b>Дата:</b> {format_datetime(task['due_date'])}\n"
    
    if task.get('location'):
        text += f"<b>Место:</b> {task['location']}\n"
    
    await callback.message.edit_text(
        text,
        reply_markup=get_task_actions_keyboard(task_id),
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(F.data.startswith("edit_task_"))
async def callback_edit_task(callback: CallbackQuery):
    """Редактирование задачи."""
    task_id = int(callback.data.replace("edit_task_", ""))
    
    await callback.message.edit_text(
        f"✏️ <b>Редактирование задачи #{task_id}</b>\n\n"
        "Функция редактирования будет реализована позже.",
        reply_markup=get_task_actions_keyboard(task_id),
        parse_mode="HTML"
    )
    await callback.answer("Редактирование в разработке")


@router.callback_query(F.data.startswith("delete_task_"))
async def callback_delete_task(callback: CallbackQuery):
    """Подтверждение удаления задачи."""
    task_id = int(callback.data.replace("delete_task_", ""))
    
    await callback.message.edit_text(
        f"🗑 <b>Удаление задачи</b>\n\n"
        f"Вы уверены, что хотите удалить задачу #{task_id}?",
        reply_markup=get_confirm_delete_keyboard(task_id),
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(F.data.startswith("confirm_delete_"))
async def callback_confirm_delete(callback: CallbackQuery):
    """Подтверждённое удаление задачи."""
    task_id = int(callback.data.replace("confirm_delete_", ""))
    
    # Здесь будет удаление из БД
    # Пока заглушка
    
    await callback.message.edit_text(
        f"✅ <b>Задача #{task_id} удалена</b>",
        reply_markup=get_main_menu()
    )
    await callback.answer("Задача удалена")


@router.callback_query(F.data.startswith("send_task_"))
async def callback_send_task(callback: CallbackQuery):
    """Отправка задачи в интеграции."""
    task_id = int(callback.data.replace("send_task_", ""))
    
    from bot.keyboards.destinations import get_destinations_keyboard
    await callback.message.edit_text(
        f"📤 <b>Отправка задачи #{task_id}</b>\n\n"
        "Выберите, куда отправить:",
        reply_markup=get_destinations_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(F.data.startswith("tasks_page_"))
async def callback_tasks_page(callback: CallbackQuery):
    """Пагинация списка задач."""
    page = int(callback.data.replace("tasks_page_", ""))
    
    # Здесь будет запрос к БД с пагинацией
    tasks = [
        {"id": 1, "title": "Пример задачи 1"},
        {"id": 2, "title": "Пример задачи 2"},
    ]
    
    await callback.message.edit_text(
        f"📋 <b>Мои задачи</b>\n\n"
        f"Страница {page + 1}",
        reply_markup=get_tasks_list_keyboard(tasks, page=page),
        parse_mode="HTML"
    )
    await callback.answer()
