import aiohttp
from local_settings import WORDS_RANDOM


async def get_random():
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_RANDOM) as response:
            return await response.json()