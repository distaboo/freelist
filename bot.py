from telebot import types
import requests
import telebot
from telebot.types import Message

TOKEN = "751120059:AAGGNfinmmdqDNYLyL2hP-FeeiMnCF3vp3E"
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 1)
btn_adress = types.KeyboardButton('Список магазинов',request_location = True)
btn_payment = types.KeyboardButton('Способы оплаты')
btn_delivery = types.KeyboardButton('Способы доставки')
markup_menu.add(btn_adress,btn_payment,btn_delivery)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Hello', reply_markup=markup_menu)

@bot.edited_message_handler(content_types=['text'])
@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
        bot.reply_to(message, 'Alex is good kid')
        return

bot.polling(timeout=60)