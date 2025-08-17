from logging import exception
from main import get_pussy_pic
from aiogram import Router
from aiogram.types import Message

router = Router(name=__name__)

@router.message()
async def main_handler(message: Message):
    try:
        if message.text == 'more pussy':
            await message.answer_photo(photo=f'https://cataas.com/cat/{await get_pussy_pic()}')
        else:
            await message.answer("Sorry, bro, but I don't know how to do anything else but throw pussy...")
            await message.answer_sticker('CAACAgQAAxkBAAENqetnmna2yveoBoqErzSjrtOJyZcsHQACnRUAAtKA0VIkyAO50FdLtTYE')
    except exception as e:
        print(e)
        await message.answer('Sorry, bro, something went wrong')
        await message.answer_sticker('CAACAgQAAxkBAAENqetnmna2yveoBoqErzSjrtOJyZcsHQACnRUAAtKA0VIkyAO50FdLtTYE')