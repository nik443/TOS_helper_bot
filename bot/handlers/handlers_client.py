from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

from bot.bot_telegram import bot, dp
from bot.keyboards.client_kb import kb_client
from bot.data_base import sql_dp


async def command_start(message: Message):
    await bot.send_message(
        message.from_user.id,
        'Дорогой хабаровчанин, в этом чате я могу ответить на большинство вопросов, касательно такой классной штуки, '
        'как ТОС. А если вдруг я не смогу ответить на твой вопрос, то ты можешь задать его сотрунику мэрии, контактная '
        'информация есть под соответствующей кнопкой в меню',
        reply_markup=kb_client
    )


async def get_frequently_question(message: Message):
    await sql_dp.get_all_faq(message)


@dp.message_handler(lambda message: '/OTBET_' in message.text)
async def answers_the_frequently_question(message: Message):
    await sql_dp.get_answer_the_frequently_question(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(get_frequently_question, commands=['Частые_вопросы'])
