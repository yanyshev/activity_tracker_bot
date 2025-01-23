import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set!")

KEY_IDENTIFIER = os.getenv('KEY_IDENTIFIER')
if not KEY_IDENTIFIER:
    raise ValueError("KEY_IDENTIFIER is not set!")

YAGPT_KEY = os.getenv('YAGPT_KEY')
if not YAGPT_KEY:
    raise ValueError("YAGPT_KEY is not set!")

CATALOG_IDENTIFIER = os.getenv('CATALOG_IDENTIFIER')
if not CATALOG_IDENTIFIER:
    raise ValueError("CATALOG_IDENTIFIER is not set!")

IAM_TOKEN = os.getenv('IAM_TOKEN')
if not CATALOG_IDENTIFIER:
    raise ValueError("IAM_TOKEN is not set!")