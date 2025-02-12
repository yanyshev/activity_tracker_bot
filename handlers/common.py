from aiogram import Router, types
from aiogram.filters import Command
from utils.data_storage import users
from aiogram.enums import ParseMode

router = Router()

def setup_handlers(dp):
    dp.include_router(router)

# /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Hello, <b>{message.from_user.full_name}</b>!\n"
        "I can calculate your activity, calories and water consumption\n"
        "Start setting up your profile with /set_profile", parse_mode=ParseMode.HTML)

# /help
@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.reply(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/set_profile - Set up your profile\n"
        "/check_progress - Check your progress\n"
        "/log_water - Log your water\n"
        "/log_food - Log your food\n"
        "/log_workout - Log your activity\n"
        "/help - Show this message\n")

# /check_progress
@router.message(Command("check_progress"))
async def cmd_check_progress(message: types.Message):
    user_id = str(message.from_user.id)
    if user_id not in users:
        await message.answer("Set up your profile first: /set_profile")
        return

    data = users[user_id]
    response = (
        "Here's your profile:\n"
        f"City: {data.get('city')}\n"
        f"Weight: {data.get('weight')}\n"
        f"Height: {data.get('height')}\n"
        f"Age: {data.get("age")}\n"
        "\n"
        "<b>Your water consumption progress:</b>\n"
        f"Water logged: {data.get('water_logged')}\n"
        f"Water goal: {data.get('water_goal')}\n"
        "\n"
        "<b>Your calories progress:</b>\n"
        f"Calories logged: {data.get('calories_logged')}\n"
        f"Calories goal: {data.get('calories_goal')}\n"
        f"Calories burned: {data.get('calories_burned')}\n")

    await message.reply(response, parse_mode=ParseMode.HTML)