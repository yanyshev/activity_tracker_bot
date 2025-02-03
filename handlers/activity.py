from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils.data_storage import users
from utils.src import get_food_info
from utils.states import FoodForm
from utils.src import workout_calories_per_min
from utils.states import ProcessFoodWeight

activity_router = Router()

# /log_water
@activity_router.message(Command("log_water"))
async def cmd_log_water(message: types.Message):
    user_id = str(message.from_user.id)
    user_response = message.text.strip().split()
    if len(user_response) < 2 or not user_response[1].isdigit():
        await message.answer("Please consider the input format: /log_water <amount in ml>")
        return
    amount = int(user_response[1])

    if user_id not in users:
        await message.answer("Set up your profile first: /set_profile")
        return

    users[user_id]["logged_water"] += amount
    remaining = max(0, users[user_id]["water_goal"] - users[user_id]["logged_water"])
    await message.answer(
            f"You've logged {amount} ml. Remaining to reach the goal: {remaining} ml."
        )

# /log_food
@activity_router.message(Command("log_food"))
async def cmd_log_food(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    user_response = message.text.strip().split()
    if len(user_response) < 2:
        await message.answer("Please consider the input format: /log_food <food product>")
        return
    product = user_response[1]

    if user_id not in users:
        await message.answer("Set up your profile first: /set_profile")
        return

    nutrition_info = int(get_food_info(product).get('calories'))
    if nutrition_info is None:
        await message.answer("No nutrition info available. Correct the input or try another product")
        return
    else:
        await state.update_data(name=product)
        await state.update_data(calories=nutrition_info)
        await message.reply(
            f"We found {product} with {nutrition_info} per 100 g.\n"
            "How much did you eat? g")
        await state.set_state(ProcessFoodWeight.food_weight)

@activity_router.message(ProcessFoodWeight.food_weight)
async def get_food_weight(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    if not message.text.isdigit():
        await message.answer("Please input weight in digits")
        return
    data = await state.get_data()
    weight = int(message.text)
    total_calories = (data['calories'] / 100) * weight
    users[user_id]["logged_calories"] += total_calories
    await state.update_data(food_weight=message.text)
    await message.answer(
        f"Written down: {total_calories:.1f} kcal. "
        f"Progress so far: {users[user_id]['logged_calories']:.1f} kcal."
    )
    await state.clear()

# /log_workout
@activity_router.message(Command("log_workout"))
async def cmd_log_workout(message: types.Message):
    user_id = str(message.from_user.id)
    args = message.text.split(maxsplit=2)

    if len(args) < 3 or not args[2].isdigit():
        await message.answer("Please use the correct format: /log_workout <workout_type> <duration>")
        return

    if user_id not in users:
        await message.answer("Set up your profile first: /set_profile")
        return

    workout_type = args[1].lower()
    duration = int(args[2])

    if workout_type not in workout_calories_per_min:
        await message.answer(f"Unknown workout type '{workout_type}'. Please choose from: {', '.join(workout_calories_per_min.keys())}.")
        return

    calories_burned = workout_calories_per_min[workout_type] * duration

    users[user_id]["activity"] += calories_burned

    await message.answer(
        f"Workout logged: {workout_type.capitalize()} for {duration} minutes.\n"
        f"Calories burned: {calories_burned} kcal.\n"
    )

