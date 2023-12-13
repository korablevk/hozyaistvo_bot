from aiogram.fsm.state import State, StatesGroup


class Greeting(StatesGroup):
    greeting = State()


class Category(StatesGroup):
    category = State()


class SubCategory(StatesGroup):
    chicken = State()
    ducks = State()
    gooses = State()


class Chicken(StatesGroup):
    meat_egg = State()
    meat = State()
    egg = State()


class ChickenMeat(StatesGroup):
    meat_egg = State()
    meat = State()
    egg = State()


class ChickenMeatEgg(StatesGroup):
    meat_egg = State()
    meat = State()
    egg = State()


class ChickenEgg(StatesGroup):
    meat_egg = State()
    meat = State()
    egg = State()


class Ducks(StatesGroup):
    meat_egg = State()
    meat = State()
    egg = State()


class Gooses(StatesGroup):
    meat_egg = State()
    meat = State()
    egg = State()


class Scrolls(StatesGroup):
    MAIN = State()
    PAGERS = State()
    STUB = State()


