from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton('/Частые_вопросы')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1)



