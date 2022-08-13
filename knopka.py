from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from importlib.resources import path
from pathlib import Path
tugma1 = InlineKeyboardButton('🇺🇿 Õzbek tili', callback_data="uz")
tugma2 = InlineKeyboardButton('🇷🇺 Русский язык', callback_data="ru")
tugma3 = InlineKeyboardButton('🇺🇸 English', callback_data="eng")



Natija = InlineKeyboardMarkup().row(tugma1, tugma2, tugma3)

#.add(tel,lok)

menu = KeyboardButton(text='🍽 Menyu')
call = KeyboardButton(text='☎️Qòngìroq-markazi')
tel = KeyboardButton(text='Tel raqamini  yuborish', request_contact=True)
lok = KeyboardButton(text='Lokatsiyani yuborish', request_location=True)
soz = KeyboardButton(text='⚙️Sozlamamlar')
Natija_uz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(menu,tel, lok, call).row(soz)



orq = KeyboardButton(text='⬅️Ortga qaytish')
men = KeyboardButton(text='Tilni òzgartirish')
soz_uz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(men,orq)


#🍟🌭🍔🍕🥪🥙🍱🍫☕️🍗🌶
pizza =KeyboardButton(text='🍕 Pitsa')
shaurm=KeyboardButton(text='🥙 Shaurma')
zakus= KeyboardButton(text='🍟 Zakuskalar')
ichim= KeyboardButton(text='☕️ Ichimliklar')
donar= KeyboardButton(text='🍱 Setlar')
hdog = KeyboardButton(text='🌭 Hot-dog')
sandwich=KeyboardButton(text='🥪 Sandvich')
gamburg=KeyboardButton(text='🍔 Burgerlar')
shirin =KeyboardButton(text='🍫 Shirinliklar')
menu_uz=ReplyKeyboardMarkup(resize_keyboard=True).add(pizza,shaurm,zakus,ichim,donar,hdog,sandwich,gamburg,shirin).row(orq)


menu = KeyboardButton(text='🍽 Menu')
call = KeyboardButton(text='☎️Call-center')
tel = KeyboardButton(text='Send phone number', request_contact=True)
lok = KeyboardButton(text='Send location', request_location=True)
soz = KeyboardButton(text='⚙️Settings')
Natija_eng = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(menu,tel, lok, call).row(soz)

pizza = KeyboardButton(text='🍕 Pizza')
shaurm = KeyboardButton(text='🥙 Shaurma')
zakus = KeyboardButton(text='🍟 Potato free')
ichim = KeyboardButton(text='☕️ Drinks')
donar = KeyboardButton(text='🍱 Salads')
hdog = KeyboardButton(text='🌭 Hot-dog')
sandwich = KeyboardButton(text='🥪 Sandwich')
gamburg = KeyboardButton(text='🍔 Burgers')
shirin = KeyboardButton(text='🍫 Sweets')
menu_eng = ReplyKeyboardMarkup(resize_keyboard=True).add(pizza, shaurm, zakus, ichim, donar, hdog, sandwich, gamburg, shirin).row(orq)

orq = KeyboardButton(text='⬅️Назад')
men = KeyboardButton(text='Change laungage')
soz_eng = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(men,orq)

menu = KeyboardButton(text='🍽 Меню')
call = KeyboardButton(text='☎️Колл-центер')
tel = KeyboardButton(text='Отправить номер телефона', request_contact=True)
lok = KeyboardButton(text='Отправить местоположение', request_location=True)
soz = KeyboardButton(text='⚙️Настройки')
Natija_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(menu,tel, lok, call).row(soz)

pizza =KeyboardButton(text='🍕 Пицца')
shaurm=KeyboardButton(text='🥙 Шаурма')
zakus= KeyboardButton(text='🍟 Закуски')
ichim= KeyboardButton(text='☕️ Напиткм')
donar= KeyboardButton(text='🍱 Салаты')
hdog = KeyboardButton(text='🌭 Хот-доги')
sandwich=KeyboardButton(text='🥪 Сендвичи')
gamburg=KeyboardButton(text='🍔 Бургеры')
shirin =KeyboardButton(text='🍫 Сладости')
menu_ru=ReplyKeyboardMarkup(resize_keyboard=True).add(pizza,shaurm,zakus,ichim,donar,hdog,sandwich,gamburg,shirin).row(orq)

orq = KeyboardButton(text='⬅️Return')
men = KeyboardButton(text='Изменить язык')
soz_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(men,orq)















































































