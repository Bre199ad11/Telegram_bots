import telebot
from telebot import types # для указание типов

from PIL import Image, ImageFilter

import time

bot = telebot.TeleBot('6581012402:AAEoFDiSXeAJ1Es1heqqEESd-gLgpnTt4EM')

path_to_save_photo='D:/nur_bot/photo bot/saved photo/1.jpg'
path_to_modified_photo='D:/nur_bot/photo bot/TelegramImageTest/1.1.jpg'

#id Дениса
den_id=123704982


@bot.message_handler(commands=["start"])
def start(message):
    first_msg="Привет!"
    bot.send_message(message.chat.id, first_msg, reply_markup=None)
    second_msg="Отправь мне фото 🙏"
    bot.send_message(message.chat.id, second_msg, reply_markup=None)


@bot.message_handler(content_types=['text'])

def message(message):
    send_msg="Извините, я вас не понимаю 😔"
    bot.send_message(message.chat.id, send_msg, reply_markup=None)

@bot.message_handler(content_types=['photo'])

def photo(message):   
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    str=path_to_save_photo
    #str=path_to_save_photo+ '/' + file_info.file_id + '.jpg'
    downloaded_file = bot.download_file(file_info.file_path)
    with open(str, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, text="Фото успешно загружено", reply_markup=None)
    bot.send_photo(message.chat.id, photo=open(path_to_modified_photo, 'rb'))


bot.polling(non_stop=True)