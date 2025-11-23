"""Приём текста/голоса → парсинг → черновик."""

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot.keyboards.task_input import get_task_input_methods, get_cancel_button
from bot.keyboards.menu import get_main_menu
from utils.logger import logger

router = Router()


class TaskInputStates(StatesGroup):
    """Состояния для ввода задачи."""
    waiting_for_text = State()
    waiting_for_voice = State()


@router.callback_query(F.data == "create_task")
async def callback_create_task(callback: CallbackQuery):
    """Начало создания задачи."""
    await callback.message.edit_text(
        "➕ <b>Создание задачи</b>\n\n"
        "Выберите способ ввода:",
        reply_markup=get_task_input_methods(),
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(F.data == "input_text")
async def callback_input_text(callback: CallbackQuery, state: FSMContext):
    """Запрос текстового ввода."""
    await callback.message.edit_text(
        "✍️ <b>Введите задачу текстом</b>\n\n"
        "Например: 'Встреча с командой завтра в 15:00 в офисе'",
        reply_markup=get_cancel_button(),
        parse_mode="HTML"
    )
    await state.set_state(TaskInputStates.waiting_for_text)
    await callback.answer()


@router.callback_query(F.data == "input_voice")
async def callback_input_voice(callback: CallbackQuery, state: FSMContext):
    """Запрос голосового ввода."""
    await callback.message.edit_text(
        "🎤 <b>Отправьте голосовое сообщение</b>\n\n"
        "Произнесите задачу, например: 'Встреча с командой завтра в 15:00'",
        reply_markup=get_cancel_button(),
        parse_mode="HTML"
    )
    await state.set_state(TaskInputStates.waiting_for_voice)
    await callback.answer()


@router.message(TaskInputStates.waiting_for_text)
async def process_text_input(message: Message, state: FSMContext):
    """Обработка текстового ввода."""
    text = message.text
    
    if not text or len(text.strip()) == 0:
        await message.answer("Пожалуйста, введите текст задачи.")
        return
    
    # Сохраняем текст в состояние
    await state.update_data(task_text=text, input_method="text")
    
    # Здесь будет вызов парсера, пока просто переходим к подтверждению
    await message.answer(
        f"📝 <b>Задача получена:</b>\n\n{text}\n\n"
        "Обрабатываю...",
        parse_mode="HTML"
    )
    
    # Переход к подтверждению
    # Импортируем здесь, чтобы избежать циклических зависимостей
    from bot.handlers.task_confirmation import show_task_draft
    await show_task_draft(message, state)


@router.message(TaskInputStates.waiting_for_voice, F.voice)
async def process_voice_input(message: Message, state: FSMContext):
    """Обработка голосового ввода."""
    voice = message.voice
    
    await message.answer("🎤 Обрабатываю голосовое сообщение...")
    
    # Здесь будет вызов Whisper для распознавания
    # Пока заглушка
    transcribed_text = "[Распознанный текст будет здесь]"
    
    await state.update_data(task_text=transcribed_text, input_method="voice")
    
    await message.answer(
        f"📝 <b>Распознано:</b>\n\n{transcribed_text}\n\n"
        "Обрабатываю...",
        parse_mode="HTML"
    )
    
    # Переход к подтверждению
    from bot.handlers.task_confirmation import show_task_draft
    await show_task_draft(message, state)
