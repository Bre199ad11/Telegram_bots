import telebot
from telebot import types # для указание типов

from PIL import Image, ImageFilter

import time

import datetime
from datetime import datetime

import pandas as pd

import os

bot = telebot.TeleBot('6581012402:AAEoFDiSXeAJ1Es1heqqEESd-gLgpnTt4EM')

path_to_folder='D:/nur_bot/photo bot/saved photo/'

path_to_statistic='D:/nur_bot/photo bot/data.csv'

start_stop=True


#id Дениса
den_id=123704982
my_id=644440906

@bot.message_handler(commands=["start"])
def start(message):
    first_msg="Привет!"
    bot.send_message(message.chat.id, first_msg, reply_markup=None)
    second_msg="Отправь мне фото и я его обработаю)"
    bot.send_message(message.chat.id, second_msg, reply_markup=None)


@bot.message_handler(content_types=['text'])

def message(message):
    if (message.text=='root' and (message.chat.id==den_id or message.chat.id==my_id)):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(types.KeyboardButton("Start/stop"))
        markup.add(types.KeyboardButton("Clear all"))
        markup.add(types.KeyboardButton("Cooldown"))
        markup.add(types.KeyboardButton("Устновить лимит"))
        markup.add(types.KeyboardButton("Exit"))
        bot.send_message(message.chat.id, text="ROOT: Вы вошли с правами root",reply_markup=markup)

    #выход их рут прав
    elif(message.text=="Exit" and (message.chat.id==my_id or message.chat.id==den_id)):
        markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(types.KeyboardButton("OK"))
        bot.send_message(message.chat.id, text="Теперь вы обычный пользователь", reply_markup=markup)
    
    #on-off bot
    elif (message.text=='Start/stop' and (message.chat.id==den_id or message.chat.id==my_id)):
        if (start_stop==True): 
            #global start_stop
            start_stop=False
            bot.send_message(message.chat.id, text="ROOT: bot is OFF", reply_markup=None)
        else:
            #global start_stop
            start_stop=True
            bot.send_message(message.chat.id, text="ROOT: bot is ON", reply_markup=None)

    #cooldown
    elif (message.text=='Cooldown' and (message.chat.id==den_id or message.chat.id==my_id)):
        bot.send_message(message.chat.id, text="Задержка на 60 секунд", reply_markup=None)
        time.sleep(60)


    else:
        send_msg="Извините, я вас не понимаю 😔"
        bot.send_message(message.chat.id, send_msg, reply_markup=None)

@bot.message_handler(content_types=['photo'])

def photo(message):   
    if (start_stop==True):
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        path_to_save=path_to_folder+str(message.chat.id)
        if (os.path.exists(path_to_save)==False):
            os.mkdir(path_to_save)
        s=path_to_save+'/'+'1.jpg'
        #str=path_to_save_photo+ '/' + file_info.file_id + '.jpg'
        downloaded_file = bot.download_file(file_info.file_path)
        if (os.path.exists(s)):
            os.remove(s)
        with open(s, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, text="Фото успешно загружено", reply_markup=None)
        statistics_write(message.chat.id, message.chat.username)
        path_to_send=path_to_folder+str(message.chat.id)+'/'+'1.1.jpg'
        bot.send_photo(message.chat.id, photo=open(path_to_send, 'rb'))
        bot.send_message(message.chat.id, text="Можешь еще раз отправить фото :D", reply_markup=None)


def statistics_write(user_id, username):
    data = datetime.today().strftime("%Y-%m-%d-%H-%M")
    statistics={'data': [data],
                'user_id': [user_id],
                'username': [username]}  
    df = pd.DataFrame(statistics)
    #print(df)
    #df.to_csv(path_to_statistic, index = False) 
    old_df = pd.read_csv(path_to_statistic)
    result=pd.concat([old_df,df])
    result.to_csv(path_to_statistic, index = False)     

bot.polling(non_stop=True)