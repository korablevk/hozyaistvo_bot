from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup

from aiogram import Router
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Dialog, Window, setup_dialogs, DialogManager, ChatEvent, StartMode, ShowMode
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import (Checkbox, Button, Row, Cancel, Start, Back, SwitchTo, ManagedCheckbox,
    CurrentPage, FirstPage, LastPage, Multiselect, NextPage, NumberedPager,
    PrevPage, Row, ScrollingGroup, StubScroll, SwitchTo,
)
from aiogram_dialog.widgets.media import StaticMedia
from states import states

from .subcategory.chicken import stub_scroll_window_for_egg_chicken, stub_scroll_window_for_egg_meat_chicken, stub_scroll_window_for_meat_chicken
from .subcategory.duck import stub_scroll_window_for_egg_duck, stub_scroll_window_for_meat_duck, stub_scroll_window_for_egg_meat_duck
from .subcategory.goose import stub_scroll_window_for_egg_goose, stub_scroll_window_for_meat_goose, stub_scroll_window_for_egg_meat_goose

EXTEND_BTN_ID = "extend"

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
            Start(Const('Яичные'), id='egg', state=states.ChickenEgg.STUB),
            Start(Const('Мясо-яичные'), id='meat_egg', state=states.ChickenMeatEgg.STUB),
            Start(Const('Мясные'), id='meat', state=states.ChickenMeat.STUB),
        ),
        Start(Const("Назад"), id="restart", state=states.Category.category),
        state=states.SubCategory.chicken
    ),
    Window(
        Format(
            "Выберите "
        ),
        Row(
            Start(Const('Яичные'), id='egg', state=states.DuckEgg.STUB),
            Start(Const('Мясо-яичные'), id='meat_egg', state=states.DuckMeatEgg.STUB),
            Start(Const('Мясные'), id='meat', state=states.DuckMeat.STUB),
        ),
        Start(Const("Назад"), id="restart", state=states.Category.category),
        state=states.SubCategory.ducks
        ),
    Window(
        Format(
            "Выберите "
        ),
        Row(
            Start(Const('Яичные'), id='egg', state=states.GoosesEgg.STUB),
            Start(Const('Мясо-яичные'), id='meat_egg', state=states.GoosesMeatEgg.STUB),
            Start(Const('Мясные'), id='meat', state=states.GoosesMeat.STUB),
        ),
        Start(Const("Назад"), id="restart", state=states.Category.category),
        state=states.SubCategory.gooses
        ),
)

chicken_egg = Dialog(
    stub_scroll_window_for_egg_chicken
)

chicken_egg_meat = Dialog(
    stub_scroll_window_for_egg_meat_chicken
)

chicken_meat = Dialog(
    stub_scroll_window_for_meat_chicken
)

duck_egg = Dialog(
    stub_scroll_window_for_egg_duck
)

duck_egg_meat = Dialog(
    stub_scroll_window_for_egg_meat_duck
)

duck_meat = Dialog(
    stub_scroll_window_for_meat_duck
)

goose_egg = Dialog(
    stub_scroll_window_for_egg_goose
)

goose_egg_meat = Dialog(
    stub_scroll_window_for_egg_meat_goose
)

goose_meat = Dialog(
    stub_scroll_window_for_meat_goose
)

router = Router()
router.include_routers(category,
                       subcategory,
                       chicken_egg,
                       chicken_egg_meat,
                       chicken_meat,
                       duck_egg,
                       duck_meat,
                       duck_egg_meat)


@router.message(Command('begin'))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(states.Category.category, mode=StartMode.NEW_STACK, show_mode=ShowMode.DELETE_AND_SEND)

