from aiogram import Router, types
from aiogram.filters import Command
from utils.data_storage import users

router = Router()

# /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply(
        "Hello!\n"
        "I can calculate your activity, calories and water consumption\n"
        "Start setting up your profile with /set_profile")

# /help
@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.reply(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/set_profile - Set up your profile\n"
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
        "Your progress:\n"
        "\n"
        "Water consumption:\n"
        f"- Consumed {data['logged_water']} ml of {data['water_goal']} ml\n"
        "\n"
        "Calories:\n"
        f"- Consumed {data['logged_calories']} kcal of {data['calorie_goal']} kcal\n"
        f"- Burned {data['burned_calories']} kcal\n")

    await message.reply(response)