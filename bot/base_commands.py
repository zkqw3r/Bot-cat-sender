from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
from aiogram.filters import CommandStart

router = Router(name=__name__)



def main_kb():
    kb_list = [
        [KeyboardButton(text="more pussy")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return keyboard


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello, I'm pussy-sender bot\n"
                         "tap to get pussy to see more...",
                         reply_markup=main_kb())
