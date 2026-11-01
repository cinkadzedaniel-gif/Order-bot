from dotenv import load_dotenv
import os
from aiogram import Bot

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)