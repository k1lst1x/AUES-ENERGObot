from . local_settings import API_KEY
from aiogram import Bot, Dispatcher
from .db import Database
from apscheduler.schedulers.asyncio import AsyncIOScheduler

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)
db = Database('database.db')
scheduler = AsyncIOScheduler()
