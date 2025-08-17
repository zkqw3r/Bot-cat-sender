import random
from aiogram import Router, types
import config as cfg

router = Router(name=__name__)

@router.message(cfg.any_media_filter)
async def not_text_from_user(message: types.Message):
    await message.answer_sticker(random.choice(cfg.stickers))