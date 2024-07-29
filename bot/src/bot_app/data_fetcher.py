import aiohttp
from . local_settings import TEXTS_API_URL_RANDOM, TEXTS_API_URL_NEXT

async def get_random():
    async with aiohttp.ClientSession() as session:
        async with session.get(TEXTS_API_URL_RANDOM) as response:
            return await response.json()

async def get_text(n):
    async with aiohttp.ClientSession() as session:
        url = f"{TEXTS_API_URL_NEXT}{n}"
        async with session.get(url) as response:
            return await response.json()
