from aiogram.types import ContentType, Message
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from contextlib import suppress

from aiogram import types
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)

async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()

API_TOKEN = '5308947323:AAHMgv0nh4WGeVhgCdIow4_0I7rUDwjbYcE'

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=[ContentType.NEW_CHAT_MEMBERS])
async def new_members_handler(message: Message):
    new_member = message.new_chat_members[0]
    msg = await bot.send_message(message.chat.id, f"Добро пожаловать, {new_member.mention}!\nОзнакомься с запиненным сообщением и расскажи о себе")
    await message.delete()
    asyncio.create_task(delete_message(msg, 120))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)