from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from aiogram_dialog import Window, Dialog, DialogManager, StartMode, setup_dialogs
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Checkbox, Next, SwitchTo
from aiogram_dialog.widgets.text import Const, Jinja

from states.states import Order


FINISHED_KEY = "finished"

CANCEL_EDIT = SwitchTo(
    Const("Отменить редактирование"),
    when=F["dialog_data"][FINISHED_KEY],
    id="cnl_edt",
    state=Order.preview,
)


async def next_or_end(event, widget, dialog_manager: DialogManager, *_):
    if dialog_manager.dialog_data.get(FINISHED_KEY):
        await dialog_manager.switch_to(Order.preview)
    else:
        await dialog_manager.next()


async def result_getter(dialog_manager: DialogManager, **kwargs):
    dialog_manager.dialog_data[FINISHED_KEY] = True
    options = []
    if dialog_manager.find("pink").is_checked():
        options.append("Розовые")
    if dialog_manager.find("glitter").is_checked():
        options.append("Блестки")
    if dialog_manager.find("bow").is_checked():
        options.append("С бантиком")
    return {
        "options": options,
        "title": dialog_manager.find("title").get_value(),
        "description": dialog_manager.find("description").get_value(),
    }


dialog = Dialog(
    Window(
        Const("Введите ваше имя и фамилию"),
        TextInput(id="title", on_success=next_or_end),
        CANCEL_EDIT,
        state=Order.title,
    ),
    Window(
        Const("Введите номер"),
        TextInput(id="description", on_success=next_or_end),
        CANCEL_EDIT,
        state=Order.description,
    ),
    Window(
        Const("Выберите опции"),
        Checkbox(Const("✓ Розовый"), Const("Розовый"), id="pink"),
        Checkbox(Const("✓ Блестки"), Const("Блестки"), id="glitter"),
        Checkbox(Const("✓ С бантиком"), Const("С бантиком"), id="bow"),
        Next(Const("Далее")),
        CANCEL_EDIT,
        state=Order.options,
    ),
    Window(
        Jinja(
            "<u>Вы ввели</u>:\n\n"
            "<b>Ваше имя</b>: {{title}}\n"
            "<b>Ваш номер</b>: {{description}}\n"
            "<b>Опции</b>: \n"
            "{% for item in options %}"
            "• {{item}}\n"
            "{% endfor %}"
        ),
        SwitchTo(Const("Изменить имя"), state=Order.title, id="to_title"),
        SwitchTo(Const("Изменить номер"), state=Order.description, id="to_desc"),
        SwitchTo(Const("Изменить опции"), state=Order.options, id="to_opts"),
        state=Order.preview,
        getter=result_getter,
        parse_mode="html",
    ),
)

router = Router()
router.include_router(dialog)


@router.message(Command('order'))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(Order.title)