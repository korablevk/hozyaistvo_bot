from aiogram_dialog import Dialog, Window, setup_dialogs, DialogManager, ChatEvent, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Cancel, NumberedPager, StubScroll
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.media import StaticMedia

from states import states

from lexicon.lexicon_ru import GOOSE_EGG_TEXT, GOOSE_MEAT_TEXT, GOOSE_EGG_MEAT_TEXT

ID_STUB_SCROLL_EGG = "stub_scroll"
ID_STUB_SCROLL_MEAT_EGG = "stub_scroll"
ID_STUB_SCROLL_MEAT = "stub_scroll"


async def paging_getter_for_egg_goose(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL_EGG).get_page()
    return {
        "pages": 1,
        "current_page": GOOSE_EGG_TEXT[current_page + 1],
        "media_page": current_page + 1
    }


async def paging_getter_for_meat_egg_goose(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL_MEAT_EGG).get_page()
    return {
        "pages": 1,
        "current_page": GOOSE_EGG_MEAT_TEXT[current_page + 1],
        "media_page": current_page + 1
    }


async def paging_getter_for_meat_goose(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find(ID_STUB_SCROLL_MEAT).get_page()
    return {
        "pages": 1,
        "current_page": GOOSE_MEAT_TEXT[current_page + 1],
        "media_page": current_page + 1
    }


SCROLLS_MAIN_MENU_BUTTON = Cancel(
    text=Const("Назад"), id="back"
)

stub_scroll_window_for_egg_goose = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL_EGG, pages="pages"),
    StaticMedia(path=Format("media/gooses/egg/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL_EGG,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.GoosesEgg.STUB,
    getter=paging_getter_for_egg_goose,
    preview_data=paging_getter_for_egg_goose,
)


stub_scroll_window_for_egg_meat_goose = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL_MEAT_EGG, pages="pages"),
    StaticMedia(path=Format("media/gooses/egg_meat/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL_MEAT_EGG,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.GoosesMeatEgg.STUB,
    getter=paging_getter_for_meat_egg_goose,
    preview_data=paging_getter_for_meat_egg_goose,
)

stub_scroll_window_for_meat_goose = Window(
    Format("{current_page}"),
    StubScroll(id=ID_STUB_SCROLL_MEAT, pages="pages"),
    StaticMedia(path=Format("media/gooses/meat/{media_page}.jpg")),
    NumberedPager(
        scroll=ID_STUB_SCROLL_MEAT,
    ),
    SCROLLS_MAIN_MENU_BUTTON,
    state=states.GoosesMeat.STUB,
    getter=paging_getter_for_meat_goose,
    preview_data=paging_getter_for_meat_goose,
)