from aiogram_dialog import Dialog, Window, setup_dialogs, DialogManager, ChatEvent, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Cancel, NumberedPager, StubScroll
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.media import StaticMedia

from states import states

from lexicon.lexicon_ru import DUCK_EGG_TEXT, DUCK_MEAT_TEXT, DUCK_EGG_MEAT_TEXT

ID_STUB_SCROLL_EGG = "stub_scrolll"
ID_STUB_SCROLL_MEAT_EGG = "stub_scrolll"
ID_STUB_SCROLL_MEAT = "stub_scrolll"


async def paging_getter_for_egg_duck(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL_EGG).get_page()
    return {
        "pages": 1,
        "current_page": DUCK_EGG_TEXT[current_page + 1],
        "media_page": current_page + 1
    }


async def paging_getter_for_meat_egg_duck(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL_MEAT_EGG).get_page()
    return {
        "pages": 2,
        "current_page": DUCK_EGG_MEAT_TEXT[current_page + 1],
        "media_page": current_page + 1
    }


async def paging_getter_for_meat_duck(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL_MEAT).get_page()
    return {
        "pages": 3,
        "current_page": DUCK_MEAT_TEXT[current_page + 1],
        "media_page": current_page + 1
    }


SCROLLS_MAIN_MENU_BUTTON = Cancel(
    text=Const("Назад"), id="back"
)

stub_scroll_window_for_egg_duck = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL_EGG, pages="pages"),
    StaticMedia(path=Format("media/ducks/egg/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL_EGG,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.DuckEgg.STUB,
    getter=paging_getter_for_egg_duck,
    preview_data=paging_getter_for_egg_duck,
)


stub_scroll_window_for_egg_meat_duck = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL_MEAT_EGG, pages="pages"),
    StaticMedia(path=Format("media/ducks/egg_meat/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL_MEAT_EGG,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.DuckMeatEgg.STUB,
    getter=paging_getter_for_meat_egg_duck,
    preview_data=paging_getter_for_meat_egg_duck,
)

stub_scroll_window_for_meat_duck = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL_MEAT, pages="pages"),
    StaticMedia(path=Format("media/ducks/meat/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL_MEAT,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.DuckMeat.STUB,
    getter=paging_getter_for_meat_duck,
    preview_data=paging_getter_for_meat_duck,
)