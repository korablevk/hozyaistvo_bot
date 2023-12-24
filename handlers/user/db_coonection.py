"""Сервер Telegram бота, запускаемый непосредственно"""
from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from exception import exceptions
import services.expenses as expenses
from exception.categories import Categories
from config_data.config import Config, load_config


router = Router()