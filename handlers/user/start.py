from aiogram.filters import CommandStart

from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import Message

from aiogram_dialog import DialogManager, Dialog, Window

from lexicon.lexicon_ru import GREETING_TEXT

router = Router()


@router.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    await message.answer(GREETING_TEXT['greeting'])


