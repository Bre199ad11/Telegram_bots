import telebot
from telebot import types # для указание типов

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import time

import datetime
from datetime import datetime

import pandas as pd

import os


BOT_TOKEN='6581012402:AAEoFDiSXeAJ1Es1heqqEESd-gLgpnTt4EM'

bot = telebot.TeleBot(BOT_TOKEN)

path_to_statistic='D:/nur_bot/registration bot/data.csv'

start_stop=True


#id Дениса
den_id=123704982
my_id=644440906

class registration(StatesGroup):
    fio_ans = State() 
    phone_ans = State()
    company_ans= State()
    age_ans= State()


@bot.message_handler(commands=["start"])
def start(message):
    first_msg="Привет!"
    bot.send_message(message.chat.id, first_msg, reply_markup=None)
    second_msg="""Вас приветствует ригистрационный бот на ТАКОЕ-ТО мероприятие!
Для того, чтобы начать регистрацию введите /register"""
    # markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.add(types.KeyboardButton("Да"))
    # markup.add(types.KeyboardButton("Нет"))
    bot.send_message(message.chat.id, second_msg, reply_markup=None)


@bot.message_handler(commands=["register"])
def register_start(message):
    if (check_user(message.chat.id)=='not_passed'):
        bot.reply_to(message, 'Введите ваше ФИО:')
        bot.register_next_step_handler(message, register_name)
    else:
        bot.send_message(message.chat.id, text='Вы уже прошли регистрацию!', reply_markup=None)

# Функция-обработчик ввода ФИО
def register_name(message):
    name = message.text
    bot.reply_to(message, 'Введите компанию, где вы работаете/учитесь:')
    bot.register_next_step_handler(message, register_company, name)

# Функция-обработчик ввода комании
def register_company(message, name):
    company = message.text
    bot.reply_to(message, 'Введите ваш возраст:')
    bot.register_next_step_handler(message, register_age, name, company)

# Функция-обработчик ввода возраста
def register_age(message, name, company):
    age = message.text
    if (age.isdigit() and int(age) >= 120):
        bot.reply_to(message, 'Некорректный возраст!')
        bot.send_message(message.chat.id, text='Введите ваш возраст:', reply_markup=None)
        bot.register_next_step_handler(message, register_age, name, company)
    else:
        statistics_write(message.chat.id, message.chat.username, name, company, age)
        # Отправляем данные пользователю
        bot.send_message(message.chat.id, text= f'Вы успешно зарегистрированы!\n\nИмя: {name}\nКомпания: {company}\nВозраст: {age}',  reply_markup=None)

@bot.message_handler(content_types=['text'])
def message(message):
    if (message.text=='root' and (message.chat.id==den_id or message.chat.id==my_id)):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(types.KeyboardButton("Start/stop"))
        markup.add(types.KeyboardButton("Clear data.csv"))
        markup.add(types.KeyboardButton("Cooldown"))
        markup.add(types.KeyboardButton("Exit"))
        bot.send_message(message.chat.id, text="ROOT: Вы вошли с правами root",reply_markup=markup)

    #выход их рут прав
    elif(message.text=="Exit" and (message.chat.id==my_id or message.chat.id==den_id)):
        bot.send_message(message.chat.id, text="Теперь вы обычный пользователь", reply_markup=None)
    
    #on-off bot
    elif (message.text=='Start/stop' and (message.chat.id==den_id or message.chat.id==my_id)):
        global start_stop
        if (start_stop): 
            start_stop=False
            bot.send_message(message.chat.id, text="ROOT: bot is OFF", reply_markup=None)
        else:
            start_stop=True
            bot.send_message(message.chat.id, text="ROOT: bot is ON", reply_markup=None)

    elif (message.text=='Clear data.csv' and (message.chat.id==den_id or message.chat.id==my_id)):
        statistics={'data': [1],
                'user_id': [1],
                'username': [1],
                'name': [1],
                'company': [1],
                'age':[1]}  
        cldf=pd.read_csv(path_to_statistic)
        cldf= cldf[0:0] 
        cldf.to_csv(path_to_statistic, index = False)
        bot.send_message(message.chat.id, text="ROOT: Файл data.csv были успешно очищен. Теперь пользователи могут проходить регистрацию повторно.",
                          reply_markup=None)

    #cooldown
    elif (message.text=='Cooldown' and (message.chat.id==den_id or message.chat.id==my_id)):
        bot.send_message(message.chat.id, text="Задержка на 60 секунд", reply_markup=None)
        time.sleep(60)


    else:
        send_msg="Извините, я вас не понимаю 😔"
        bot.send_message(message.chat.id, send_msg, reply_markup=None)
        bot.send_message(message.chat.id, text="Я вас не понимаю 😢", reply_markup=None)

#запись статистики
def statistics_write(user_id, username, name, company, age):
    data = datetime.today().strftime("%Y-%m-%d-%H-%M")
    statistics={'data': [data],
                'user_id': [user_id],
                'username': [username],
                'name': [name],
                'company': [company],
                'age':[age]}  
    df = pd.DataFrame(statistics)
    #print(df)
    #df.to_csv(path_to_statistic, index = False) 
    old_df = pd.read_csv(path_to_statistic)
    result=pd.concat([old_df,df])
    result.to_csv(path_to_statistic, index = False)   

#проверка прошел ли пользователь регистрацию
def check_user(user_id):
    df = pd.read_csv(path_to_statistic)
    text_return='not_passed'
    for num, user_from_file in enumerate(df["user_id"]):
        if (user_from_file==user_id):
            text_return='passed'
            break;
    return text_return

bot.polling(non_stop=True)