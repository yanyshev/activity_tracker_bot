from aiogram.fsm.state import State, StatesGroup

class ProfileForm(StatesGroup):
    weight = State()
    height = State()
    age = State()
    activity = State()
    city = State()
    water_goal = State()
    calories_goal = State()

class FoodForm(StatesGroup):
    name = State()
    calories = State()

class ProcessFoodWeight(StatesGroup):
    food_weight = State()