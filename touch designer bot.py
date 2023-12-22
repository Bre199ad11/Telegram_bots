import telebot
from telebot import types # для указание типов

import datetime
from datetime import datetime

import pandas as pd

import time

BOT_TOKEN='6617526717:AAE5R81RbVBkE-BJhffF_EfgmC2PNVHJaYU'

bot = telebot.TeleBot(BOT_TOKEN)

path_to_statistic='D:/nur_bot/pult/data.csv'

start_stop=True

#id Дениса
den_id=123704982
my_id=644440906

@bot.message_handler(commands=['start'])

def start(message):
    first_mess = "Привет!"
    bot.send_message(message.chat.id, first_mess, reply_markup=None)
    markup=MainMarkup() 
    bot.send_message(message.chat.id, text="choose", reply_markup=markup)

@bot.message_handler(content_types=['text'])

def func(message):
    global start_stop
    if(message.text == "вправо" and start_stop==True):
         statistics_write(message.chat.id, message.chat.username, message.text)
         markup = types.InlineKeyboardMarkup()
         bot.send_message(message.chat.id, text="вправо", reply_markup=markup)

    elif(message.text == "влево" and start_stop==True):
         statistics_write(message.chat.id, message.chat.username, message.text)
         markup = types.InlineKeyboardMarkup()
         bot.send_message(message.chat.id, text="влево", reply_markup=markup)

    elif (message.text == "вверх" and start_stop==True):
         statistics_write(message.chat.id, message.chat.username, message.text)
         markup = types.InlineKeyboardMarkup()
         bot.send_message(message.chat.id, text="вверх", reply_markup=markup)

    elif (message.text == "вниз" and start_stop==True):
         statistics_write(message.chat.id, message.chat.username, message.text)
         markup = types.InlineKeyboardMarkup()
         bot.send_message(message.chat.id, text="вниз", reply_markup=markup)

     #ROOT rigths
    elif (message.text=='root' and (message.chat.id==den_id or message.chat.id==my_id)):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(types.KeyboardButton("Start/stop"))
        markup.add(types.KeyboardButton("Clear data.csv"))
        markup.add(types.KeyboardButton("Cooldown"))
        markup.add(types.KeyboardButton("Exit"))
        bot.send_message(message.chat.id, text="ROOT: Вы вошли с правами root",reply_markup=markup)

    #выход из рут прав
    elif(message.text=="Exit" and (message.chat.id==my_id or message.chat.id==den_id)):
        markup=MainMarkup()
        bot.send_message(message.chat.id, text="Теперь вы обычный пользователь", reply_markup=markup)
    
    #on-off bot
    elif (message.text=='Start/stop' and (message.chat.id==den_id or message.chat.id==my_id)):
        #global start_stop
        if (start_stop): 
            start_stop=False
            bot.send_message(message.chat.id, text="ROOT: bot is OFF", reply_markup=None)
        else:
            start_stop=True
            bot.send_message(message.chat.id, text="ROOT: bot is ON", reply_markup=None) 

     #Clear data.csv
    elif (message.text=='Clear data.csv' and (message.chat.id==den_id or message.chat.id==my_id)):
        statistics={'data': [1],
                'user_id': [1],
                'username': [1], 
                'button': [1]}  
        cldf=pd.DataFrame(statistics)
        cldf= cldf[0:0] 
        cldf.to_csv(path_to_statistic, index = False)
        bot.send_message(message.chat.id, text="data.csv succesfully cleared", reply_markup=None) 

     #cooldown
    elif (message.text=='Cooldown' and (message.chat.id==den_id or message.chat.id==my_id)):
        bot.send_message(message.chat.id, text="Задержка на 60 секунд", reply_markup=None)
        time.sleep(60)


def statistics_write(user_id, username, msg):
    data = datetime.today().strftime("%Y-%m-%d-%H-%M")
    statistics={'data': [data],
                'user_id': [user_id],
                'username': [username], 
                'button': [msg]}  
    df = pd.DataFrame(statistics)
    #print(df)
    #df.to_csv(path_to_statistic, index = False) 
    old_df = pd.read_csv(path_to_statistic)
    result=pd.concat([old_df,df])
    result.to_csv(path_to_statistic, index = False)    

def MainMarkup():
    markup = types.InlineKeyboardMarkup()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("вправо ")
    btn2 = types.KeyboardButton("влево")
    btn3 = types.KeyboardButton("вверх")
    btn4 = types.KeyboardButton("вниз")
    markup.add(btn1, btn2, btn3, btn4)
    return markup 

try:
   bot.polling(non_stop=True, interval=2)
except Exception as e:
    print("Возникли технические неполадки. Приносим свои изменения!")