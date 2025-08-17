import logging
from aiogram import Bot, Dispatcher
import asyncio
import config


async def main():
    from routers import router as main_router

    bot = Bot(token=config.TELEGRAM_TOKEN)
    dp = Dispatcher()
    dp.include_router(main_router)
    logging.basicConfig(level=logging.INFO)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())