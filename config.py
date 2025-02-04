import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set!")

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY is not set!")