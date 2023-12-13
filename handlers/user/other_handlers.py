from aiogram import Router
from aiogram.types import Message

router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def not_correct_command(message: Message):
    await message.answer(f'Не могу разобрать что вы хотите: {message.text}')