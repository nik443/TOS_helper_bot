from aiogram.utils import executor

from bot.bot_telegram import dp
from handlers.handlers_client import register_handlers_client
from bot.data_base import sql_dp


register_handlers_client(dp)


async def on_start_bot(_):
    print('Бот вышел в онлайн')
    sql_dp.sql_start()


executor.start_polling(dp, skip_updates=True, on_startup=on_start_bot)
