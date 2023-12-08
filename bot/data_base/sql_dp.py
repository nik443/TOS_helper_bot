import sqlite3

from aiogram.types import Message

from bot.bot_telegram import bot


base = sqlite3.connect('bot_db.db')
cur = base.cursor()


def sql_start():
    if base:
        # print(cur.execute("SELECT * FROM sqlite_master where type='table'").fetchall())
        print('Успешное подключение БД')


async def get_all_faq(message: Message):
    frequently_question = cur.execute('SELECT id, question FROM faq').fetchall()
    ex = []
    for question in frequently_question:
        ex.append(f'{question[0]}. {question[1]} /OTBET_{question[0]}\n')
    ex = ''.join(ex)
    await bot.send_message(message.from_user.id, ex)


async def get_answer_the_frequently_question(message: Message):
    id_question = message.text.split('_')[1]
    answer = cur.execute(f'SELECT answer FROM faq WHERE id = {id_question}').fetchall()[0][0]
    await bot.send_message(message.from_user.id, answer)