"""Настройка роутеров и middleware."""

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from utils.logger import logger

# Импорт всех роутеров
from bot.handlers import (
    navigation,
    task_input,
    task_confirmation,
    task_management,
    integrations_ui
)


def setup_dispatcher() -> Dispatcher:
    """Настройка диспетчера с роутерами и middleware."""
    # Создаём диспетчер с хранилищем состояний
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Регистрируем роутеры
    dp.include_router(navigation.router)
    dp.include_router(task_input.router)
    dp.include_router(task_confirmation.router)
    dp.include_router(task_management.router)
    dp.include_router(integrations_ui.router)
    
    logger.info("Диспетчер настроен, роутеры зарегистрированы")
    
    return dp
