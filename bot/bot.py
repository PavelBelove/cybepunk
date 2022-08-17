
from random import randint
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

from config import TOKEN
import keybords.crib.crib as kb


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def on_startup(_):
    print('Бот в онлайне')


@dp.message_handler(commands=['start', 'help', ])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Этот бот скоро научится играть в киберпанк!')
        await message.delete()
    except:
        await message.reply('Бот не может писать первым. Пожалуйста, добавьтесь в бот по ссылке https://t.me/TelePunkBot')


@dp.message_handler(commands=['new_character', ])
async def command_start(message: types.Message):
    try:
        await message.reply("Привет!", reply_markup=kb.greet_kb)

        await message.delete()
    except:
        await message.reply('Бот не может писать первым. Пожалуйста, добавьтесь в бот по ссылке https://t.me/TelePunkBot')


@dp.message_handler(commands="1test")
async def cmd_start(message: types.Message):
    keyboard = kb.markup4
    await message.answer("Выберите цифру", reply_markup=keyboard)


@dp.message_handler(Text(equals='1️⃣'))
async def with_puree(message: types.Message):
    await message.reply('1️⃣')


@dp.message_handler(lambda message: message.text == "Без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")

# Инлайн кнопки


@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="Нажми меня", callback_data="random_d10"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)


@dp.callback_query_handler(text="random_d10")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(randint(1, 10)))
    await call.answer(text="Спасибо, что воспользовались ботом!", show_alert=True)
    # или просто await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
