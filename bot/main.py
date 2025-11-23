"""Точка входа для запуска бота."""

import asyncio
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config.settings import settings
from bot.dispatcher import setup_dispatcher
from utils.logger import logger


async def main():
    """Главная функция запуска бота."""
    # Создаём бота
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    # Настраиваем диспетчер
    dp = setup_dispatcher()
    
    # Запускаем бота
    logger.info("Бот запускается...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
