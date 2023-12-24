from aiogram_dialog import Dialog, Window, setup_dialogs, DialogManager, ChatEvent, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Cancel, NumberedPager, StubScroll
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.media import StaticMedia

from states import states

from lexicon.lexicon_ru import CHICKEN_EGG_TEXT, CHICKEN_EGG_MEAT_TEXT, CHICKEN_MEAT_TEXT

ID_STUB_SCROLL_EGG = "stub_scroll"
ID_STUB_SCROLL_MEAT_EGG = "stub_scroll"
ID_STUB_SCROLL_MEAT = "stub_scroll"


async def paging_getter_for_egg_chicken(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL_EGG).get_page()
    return {
        "pages": 4,
        "current_page": CHICKEN_EGG_TEXT[current_page + 1],
        "media_page": current_page + 1
    }


async def paging_getter_for_meat_egg_chicken(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL_MEAT_EGG).get_page()
    return {
        "pages": 3,
        "current_page": CHICKEN_EGG_MEAT_TEXT[current_page + 1],
        "media_page": current_page + 1
    }


async def paging_getter_for_meat_chicken(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL_MEAT).get_page()
    return {
        "pages": 2,
        "current_page": CHICKEN_MEAT_TEXT[current_page + 1],
        "media_page": current_page + 1
    }


SCROLLS_MAIN_MENU_BUTTON = Cancel(
    text=Const("Назад"), id="back"
)

stub_scroll_window_for_egg_chicken = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL_EGG, pages="pages"),
    StaticMedia(path=Format("media/chicken/egg/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL_EGG,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.ChickenEgg.STUB,
    getter=paging_getter_for_egg_chicken,
    preview_data=paging_getter_for_egg_chicken,
)


stub_scroll_window_for_egg_meat_chicken = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL_MEAT_EGG, pages="pages"),
    StaticMedia(path=Format("media/chicken/egg_meat/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL_MEAT_EGG,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.ChickenMeatEgg.STUB,
    getter=paging_getter_for_meat_egg_chicken,
    preview_data=paging_getter_for_meat_egg_chicken,
)

stub_scroll_window_for_meat_chicken = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL_MEAT, pages="pages"),
    StaticMedia(path=Format("media/chicken/meat/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL_MEAT,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.ChickenMeat.STUB,
    getter=paging_getter_for_meat_chicken,
    preview_data=paging_getter_for_meat_chicken,
)