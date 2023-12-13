import asyncio
import os
from typing import Dict, Any

from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup

from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Dialog, Window, setup_dialogs, DialogManager, ChatEvent, StartMode, ShowMode
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import (Checkbox, Button, Row, Cancel, Start, Back, SwitchTo, ManagedCheckbox,
    CurrentPage, FirstPage, LastPage, Multiselect, NextPage, NumberedPager,
    PrevPage, Row, ScrollingGroup, StubScroll, SwitchTo,
)
from aiogram_dialog.widgets.media import StaticMedia
from states import states

from lexicon.lexicon_ru import CHICKEN_EGG_TEXT

EXTEND_BTN_ID = "extend"
ID_STUB_SCROLL = "stub_scroll"


async def paging_getter(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL).get_page()
    return {
        "pages": 2,
        "current_page": CHICKEN_EGG_TEXT[current_page + 1],
        "media_page": current_page + 1
    }

SCROLLS_MAIN_MENU_BUTTON = Cancel(
    text=Const("Назад"), id="back"
)


async def enable_send_mode(
    event: CallbackQuery, button, dialog_manager: DialogManager, **kwargs
):
    dialog_manager.show_mode = ShowMode.SEND

category = Dialog(
    Window(
        Format(
            "Добрый день, {event.from_user.username}, выберите одну из категорий. \n"
        ),
        Start(Const('Курица'), id='chickens', state=states.SubCategory.chicken),
        Start(Const('Утки'), id='ducks', state=states.SubCategory.ducks),
        Start(Const('Гуси'), id='gooses', state=states.SubCategory.gooses),
        state=states.Category.category
    ),
)

subcategory = Dialog(
    Window(
        Format(
            "Выберите категорию птицы"
        ),
        Row(
            Start(Const('Яичные'), id='egg', state=states.Scrolls.STUB),
            Start(Const('Мясо-яичные'), id='meat_egg', state=states.Chicken.meat_egg),
            Start(Const('Мясные'), id='meat', state=states.Chicken.meat),
        ),
        Start(Const("Назад"), id="restart", state=states.Category.category),
        state=states.SubCategory.chicken
    ),
    Window(
        Format(
            "Выберите "
        ),
        Row(
            Start(Const('Яичные'), id='egg', state=states.Ducks.egg),
            Start(Const('Мясо-яичные'), id='meat_egg', state=states.Ducks.meat_egg),
            Start(Const('Мясные'), id='meat', state=states.Ducks.meat),
        ),
        Start(Const("Назад"), id="restart", state=states.Category.category),
        state=states.SubCategory.ducks
        ),
    Window(
        Format(
            "Выберите "
        ),
        Row(
            Start(Const('Яичные'), id='egg', state=states.Gooses.egg),
            Start(Const('Мясо-яичные'), id='meat_egg', state=states.Gooses.meat_egg),
            Start(Const('Мясные'), id='meat', state=states.Gooses.meat),
        ),
        Start(Const("Назад"), id="restart", state=states.Category.category),
        state=states.SubCategory.gooses
        ),
)

stub_scroll_window = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL, pages="pages"),
    StaticMedia(path=Format("media/chicken/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.Scrolls.STUB,
    getter=paging_getter,
    preview_data=paging_getter,
)

chicken = Dialog(
    stub_scroll_window
)


router = Router()


@router.message(Command('begin'))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(states.Category.category)

