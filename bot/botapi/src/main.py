from aiogram import executor
from app import dp
from bot.botapi.src import local_settings
import os

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
