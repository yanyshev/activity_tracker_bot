import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from handlers.common import router #, setup_handlers
from handlers.profile import profile_router
from handlers.activity import activity_router
from utils.middlewares import LoggingMiddleware

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)
dp.include_router(profile_router)
dp.include_router(activity_router)

dp.message.middleware(LoggingMiddleware())
# setup_handlers(dp)

async def set_persistent_menu(bot: Bot):
    commands = [
        types.BotCommand(command="start", description="Start the bot"),
        types.BotCommand(command="set_profile", description="Set up the profile"),
        types.BotCommand(command="check_progress", description="Check your progress"),
        types.BotCommand(command="log_water", description="Log water"),
        types.BotCommand(command="log_food", description="Log food"),
        types.BotCommand(command="log_workout", description="Log workout"),
        types.BotCommand(command="help", description="Show help menu"),
    ]
    await bot.set_my_commands(commands)

# New updates polling
async def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Bot is running...")
    await set_persistent_menu(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())