from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils.data_storage import users
from utils.states import ProfileForm

profile_router = Router()

# /set_profile
@profile_router.message(Command("set_profile"))
async def cmd_set_profile(message: types.message, state: FSMContext):
    user_id = str(message.from_user.id)

    if user_id not in users:
        users[user_id] = {
            "weight": None,
            "height": None,
            "age": None,
            "activity": 0,
            "city": None,
            "water_goal": 0,
            "calorie_goal": 0,
            "logged_water": 0,
            "logged_calories": 0,
            "burned_calories": 0
        }

    await message.reply("Let's set up your profile!\nWhat's your weight?")
    await state.set_state(ProfileForm.weight)

@profile_router.message(ProfileForm.weight)
async def process_weight(message: types.message, state: FSMContext):
    user_id = str(message.from_user.id)
    await state.update_data(weight=message.text)
    users[user_id]["weight"] = int(message.text)
    await message.reply("What's your height?")
    await state.set_state(ProfileForm.height)

@profile_router.message(ProfileForm.height)
async def process_height(message: types.message, state: FSMContext):
    user_id = str(message.from_user.id)
    await state.update_data(height=message.text)
    users[user_id]["height"] = int(message.text)
    await message.reply("What's your age?")
    await state.set_state(ProfileForm.age)

@profile_router.message(ProfileForm.age)
async def process_age(message: types.message, state: FSMContext):
    user_id = str(message.from_user.id)
    await state.update_data(age=message.text)
    users[user_id]["age"] = int(message.text)
    await message.reply("What's your city?")
    await state.set_state(ProfileForm.city)

@profile_router.message(ProfileForm.city)
async def process_city(message: types.message, state: FSMContext):
    user_id = str(message.from_user.id)
    await message.reply("What's your age?")
    await state.update_data(city=message.text)
    users[user_id]["city"] = message.text
    await message.reply("What's your water consumption goal?")
    await state.set_state(ProfileForm.water_goal)

@profile_router.message(ProfileForm.water_goal)
async def process_water(message: types.message, state: FSMContext):
    user_id = str(message.from_user.id)
    try:
        await state.update_data(water_goal=message.text)
        users[user_id]["water_goal"] = int(message.text)
        await message.reply("What's your calories goal?")
        await state.set_state(ProfileForm.calories_goal)
    except:
        await message.reply("Your answer cannot be converted to a number. Please try again.")

@profile_router.message(ProfileForm.calories_goal)
async def process_calories(message: types.message, state: FSMContext):
    user_id = str(message.from_user.id)
    try:
        await state.update_data(calories_goal=message.text)
        users[user_id]["calorie_goal"] = int(message.text)
        data = await state.get_data()
        await message.reply("Here's your profile:\n"
                            f"City: {data.get('city')}\n"
                            f"Weight: {data.get('weight')}\n"
                            f"Height: {data.get('height')}\n"
                            f"Water goal: {data.get('water_goal')}\n"
                            f"Calories goal: {data.get('calories_goal')}\n")
        await state.clear()
    except:
        await message.reply("Your answer cannot be converted to a number. Please try again.")