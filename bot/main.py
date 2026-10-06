import asyncio
from loader import bot, dp
from handlers.user_handlers import user_router

from aiogram import Dispatcher


def register_routers(dp: Dispatcher) -> None:
    """Registers routers."""

    dp.include_router(user_router)


async def main() -> None:
    """Entry point."""

    register_routers(dp=dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())