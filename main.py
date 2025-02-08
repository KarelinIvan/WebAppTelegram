from aiogram import Bot, Dispatcher, types, executor

from aiogram.types import WebAppInfo

from settings import TELEGRAM_TOKEN

bot = Bot(TELEGRAM_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(command=["start"])
async def start(message: types.Message):
    """ Эта функция обрабатывает команду «/start» и отправляет приветственное сообщение с кнопкой для открытия веб-страницы """
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Открыть веб страницу", web_app=WebAppInfo(url = "https://ru.wikipedia.org/wiki/"),))
    await message.answer(f"Привет, {message.from_user.first_name} рад тебя видеть!👋", reply_markup=markup)

executor.start_polling(dp)
