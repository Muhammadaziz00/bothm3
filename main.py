from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import logging
import os

load_dotenv(".env")

bot = Bot(os.environ.get('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer(f'Здравствуйте {message.from_user.full_name}')
    await message.answer("Этот бот расскажет вам информацию о курсах  в Geeks", reply_markup=button)

buttons = [
    InlineKeyboardButton('backend', callback_data='backend'),
    InlineKeyboardButton('frontent', callback_data='frontent'),
    InlineKeyboardButton('ux/ui', callback_data='ux/ui'),
    InlineKeyboardButton('android', callback_data='android'),
    InlineKeyboardButton('ios', callback_data='ios')
]

button = InlineKeyboardMarkup().add(*buttons)
@dp.callback_query_handler(lambda call: call)
async def all(call):
    if call.data == "backend":
        await backend(call.message)
    elif call.data == "frontent":
        await frontent(call.message)
    elif call.data == "ux/ui":
        await uxui(call.message)
    elif call.data == "android":
        await android(call.message)
    elif call.data == "ios":
        await ios(call.message)

        
@dp.message_handler(commands='backend')
async def backend(message:types.Message):
    await message.answer("""Backend — это внутренняя часть сайта и сервера и т.д
cтоимость 10000 сом в месяц
Обучение: 5 месяц
""")
    
@dp.message_handler(commands='frontent')
async def frontent(message:types.Message):
    await message.answer("""Frontent - это та самая «одежка» IT-сервиса, по которой встречают.
стоимость 10000 сом в месяц
обучение: 5 месяц""")

@dp.message_handler(commands='ux/ui')
async def uxui(message:types.Message):
    await message.answer("""UX -  отвечает за то, как интерфейс работает
 UI - отвечает за то, как интерфейс выглядит
стоимость 10000 сом в месяц
обучение 3 месяц""")

@dp.message_handler(commands='android')
async def android(message:types.Message):
    await message.answer("""Android - создает приложения для устройств на операционной системе Android
стоимость 10000 сом в месяц
 обучение 11 месяц""")

@dp.message_handler(commands='ios')
async def ios(message:types.Message):
    await message.answer("""IOS -  это программист, который пишет сервисы и программы для айфонов
стоимость 10000 сом в месяц
обучение 11 месяц""")
@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.reply("вот мои команды \n",reply_markup=button)
    
@dp.message_handler()
async def nothing(message:types.Message):
    await message.reply("Я вас не понял, введите /help для просмотра доступных функций.")


    
executor.start_polling(dp)