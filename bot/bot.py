from email import message
import types
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5581488554:AAH4pCP2qNVVK7vlmyf8KqIQYdcwvl0InE8')
dp = Dispatcher(bot)


def on_startup(_):
    print('Бот в онлайне')


@dp.message_handler(commands=['start', 'help', ])
async def command_start(mesage: types.Message):
    try:
        await bot.send_message(mesage.from_user.id, 'Этот бот скоро научится играть в киберпанк!')
        await message.delete()
    except:
        await message.reply('Бот не может писать первым. Пожалуйста, добавьтесь в бот по ссылке https://t.me/TelePunkBot')


@dp.message_handler(commands=['new_character', ])
async def command_start(mesage: types.Message):
    try:
        await bot.send_message(mesage.from_user.id, 'Создаем характер')
        await message.delete()
    except:
        await message.reply('Бот не может писать первым. Пожалуйста, добавьтесь в бот по ссылке https://t.me/TelePunkBot')


@dp.message_handler()
async def send(message: types.Message):

    await message.answer(message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
