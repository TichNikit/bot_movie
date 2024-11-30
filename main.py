import asyncio
import logging

from token_.my_token import token

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from user.message import register_user_messages

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    bot = Bot(token, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    register_user_messages(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
