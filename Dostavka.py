import logging
import knopka as kn
from distutils.cmd import Command
from imaplib import Commands
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, Message, InputFile
from pathlib import Path


API_TOKEN = '5471420151:AAFX1GptiCXVVf9tY8MVol81_hi8ZaDohTw'

logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
db=Dispatcher(bot)

download_path=Path().joinpath("downloads")
download_path.mkdir(parents=True, exist_ok=True)


@db.message_handler(commands=['start','restart'])
async def start(message:types.Message):
    ism=message.from_user.first_name
    await message.answer(f"Assalomu alaykum {ism}.Bu bot sizga mazzali taomlarni yetkazib berishlarida yordam beradi.", reply_markup=kn.Natija)




@db.callback_query_handler(lambda uz: uz.data =='uz')
async def innline_uz(callback_query:types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,'Siz òzbek tilini tanladingiz!', reply_markup=kn.Natija_uz)


@db.callback_query_handler(lambda ru: ru.data == 'ru')
async def innline_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали русский язык!', reply_markup=kn.Natija_ru)


@db.callback_query_handler(lambda eng: eng.data == 'eng')
async def innline_eng(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'You choosed english laungage!', reply_markup=kn.Natija_eng)

@db.message_handler()
async def standart(message:types.Message):
    if message.text == '🍽 Menyu':
        await bot.send_message(message.from_user.id, '🍽 Menyu', reply_markup=kn.menu_uz)
    if message.text == '🍽 Menu':
        await bot.send_message(message.from_user.id, '🍽 Menu', reply_markup=kn.menu_eng)
    if message.text == '🍽 Меню':
        await bot.send_message(message.from_user.id, '🍽 Меню', reply_markup=kn.menu_ru)
    if message.text == '☎️Qòngìroq-markazi':
        await bot.send_message(message.from_user.id, '☎️+(998)91-777-60-84 ',reply_markup=kn.Natija_uz)
    if message.text == '☎️Колл-центер':
        await bot.send_message(message.from_user.id, '☎️+(998)91-777-60-84 ', reply_markup=kn.Natija_ru)
    if message.text == '☎️Call-center':
        await bot.send_message(message.from_user.id, '☎️+(998)91-777-60-84 ', reply_markup=kn.Natija_eng)
    if message.text == '⬅️Ortga qaytish': 
        await bot.send_message(message.from_user.id, '⬅️Ortga qaytish',reply_markup=kn.Natija_uz)
    if message.text == '⬅️Назад':
        await bot.send_message(message.from_user.id, '⬅️Назад', reply_markup=kn.Natija_ru)
    if message.text == '⬅️Return':
        await bot.send_message(message.from_user.id, '⬅️Return', reply_markup=kn.Natija_eng)
    if message.text == '⚙️Sozlamamlar':
        await bot.send_message(message.from_user.id, '⚙️Sozlamamlar', reply_markup=kn.soz_uz)
    if message.text == '⚙️Настройки':
        await bot.send_message(message.from_user.id, '⚙️Настройки', reply_markup=kn.soz_ru)
    if message.text == '⚙️Settings':
        await bot.send_message(message.from_user.id, '⚙️Settings', reply_markup=kn.soz_eng)
    if message.text == 'Tilni òzgartirish':
        await bot.send_message(message.from_user.id, 'Tilni òzgartirish', reply_markup=kn.Natija)
    if message.text == 'Change laungage':
        await bot.send_message(message.from_user.id, 'Change laungage', reply_markup=kn.Natija)
    if message.text == 'Изменить язык':
        await bot.send_message(message.from_user.id, 'Изменить язык', reply_markup=kn.Natija)









@db.message_handler(content_types='photo')
async def echo(message: Message):
    await message.photo[-1].download(download_path)
    file_id = message.photo[-1].file_id
    await message.reply(f"Sizning foto faylingiz qabul qilindi!\ndoc_id={file_id}")


@db.message_handler(commands=['menu'])
async def send_photo(message: types.Message):
    photo_id = "AgACAgIAAxkBAAIBj2L3pNYz2voK8ZANy4Vjrcqu-9mrAAL4vzEb_DnAS9e79p_UERKqAQADAgADeAADKQQ"
    await message.reply_photo(photo_id, caption="1 Salom")


if __name__=="__main__":
    executor.start_polling(db, skip_updates=True)

















