import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher


bot = Bot(token=str(os.environ.get('BOT_TOKEN')))
dp = Dispatcher(bot)