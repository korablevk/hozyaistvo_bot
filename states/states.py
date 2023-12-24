from aiogram.fsm.state import State, StatesGroup


class Greeting(StatesGroup):
    greeting = State()


class Category(StatesGroup):
    category = State()


class SubCategory(StatesGroup):
    chicken = State()
    ducks = State()
    gooses = State()


class ChickenCross(StatesGroup):
    cross = State()
    meat_egg = State()
    meat = State()
    egg = State()


class ChickenBreed(StatesGroup):
    breed = State()
    meat_egg = State()
    meat = State()
    egg = State()


class ChickenMeat(StatesGroup):
    STUB = State()


class ChickenMeatEgg(StatesGroup):
    STUB = State()


class ChickenEgg(StatesGroup):
    STUB = State()


class DucksCross(StatesGroup):
    cross = State()
    meat_egg = State()
    meat = State()
    egg = State()


class DucksBreed(StatesGroup):
    breed = State()
    meat_egg = State()
    meat = State()
    egg = State()


class DuckMeat(StatesGroup):
    STUB = State()


class DuckMeatEgg(StatesGroup):
    STUB = State()


class DuckEgg(StatesGroup):
    STUB = State()


class GoosesCross(StatesGroup):
    cross = State()
    meat_egg = State()
    meat = State()
    egg = State()


class GoosesBreed(StatesGroup):
    breed = State()


class GoosesMeat(StatesGroup):
    STUB = State()


class GoosesMeatEgg(StatesGroup):
    STUB = State()


class GoosesEgg(StatesGroup):
    STUB = State()


class Order(StatesGroup):
    title = State()
    description = State()
    options = State()
    preview = State()