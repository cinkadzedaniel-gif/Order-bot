import aiogram
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
import asyncio
from start import stert_router
from handl.manik import manik_router
from handl.faq import faq_router
from bot import bot
from handl.support import support_router


load_dotenv()

dp = Dispatcher()

dp.include_router(stert_router)
dp.include_router(manik_router)
dp.include_router(faq_router)
dp.include_router(support_router)

async def main():
    print("БОТ ЗАПУСТИВСЯ")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())