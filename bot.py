import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.common import router #, setup_handlers
from handlers.profile import profile_router
from handlers.activity import activity_router
from handlers.common import setup_handlers
from utils.middlewares import LoggingMiddleware

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)
dp.include_router(profile_router)
dp.include_router(activity_router)

# dp.message.middleware(LoggingMiddleware())
# setup_handlers(dp)

# New updates polling
async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())