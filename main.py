import os
import telebot
from telebot import types
import qrcode

bot = telebot.TeleBot(os.getenv('QR_CODE_API_TOKEN'))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, 'Я - <b>бот</b>, который генерирует QR-код предоставленной ссылки',
                     parse_mode='html')
    bot.send_message(message.chat.id, 'Пришли ссылку, чтобы получить QR-код')


@bot.message_handler(content_types=['text'])
def message_reply(message):
    img = qrcode.make(message.text)
    img.save("qr.png")
    file = open('qr.png', 'rb')
    bot.send_photo(message.chat.id, file, "Вот твой QR-код!")


bot.infinity_polling()
