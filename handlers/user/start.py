from aiogram.filters import CommandStart, Command

from aiogram import Router
from aiogram.types import Message

from aiogram_dialog import DialogManager, Dialog, Window

from lexicon.lexicon_ru import GREETING_TEXT

router = Router()


@router.message(CommandStart())
@router.message(Command('help'))
async def start(message: Message, dialog_manager: DialogManager):
    await message.answer(GREETING_TEXT['greeting'])


