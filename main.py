import telebot
from telebot import types
import random

bot = telebot.TeleBot('5169779515:AAE1STcClE8c_2tiCRUqoHCO2qFw8CKZhSk')



@bot.message_handler(commands=['tart'])
def text_message(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(commands=['Brand'])
def text_message(message):
    HO = random.randint(2, 5)
    photo = open(f"TMP/{HO}.jpg", 'rb')
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Сайт', url='https://goo.su/amko')

    markup.add(btn_my_site)
    print(photo)
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)

@bot.message_handler(commands=['help'])
def text_message(message):
    bot.send_message(message.chat.id, 'Чем вам помочь?')


bot.polling()