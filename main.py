import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command 
from aiogram.types.bot_command import BotCommand

bot = Bot(token="7028205352:AAEUzZzpdJHlLDoabeQUvCSRIR8u99aREdM")
dp = Dispatcher()

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text="отправьте команду Играть")
    async def set_commands():
        bot_commands = [
            BotCommand(
                command="/start", description="Начало работы"),
            BotCommand(
                command="/Играть", description="Начало игры")
        ]     
        await bot.set_my_commands(bot_commands)   

@router.message(Command("Играть"))
async def photo_handler(msg: Message):
    file_path = "/Users/Home/Desktop/rpm/tgbot/pole.jpg"
    await msg.answer_photo(photo=FSInputFile(path=file_path))
    
async def main():
    await dp.start_polling(bot)

dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())
