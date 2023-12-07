import telebot
from telebot import types # для указание типов


bot = telebot.TeleBot('6581012402:AAEoFDiSXeAJ1Es1heqqEESd-gLgpnTt4EM')


"""questions = {"Кто является автором романа «Война и мир»?": ["Федор Достоевксий", "Лев Толстой", "Александр Солжнецын", "Антон Чехов"], 
             "Какое животное считается символом мудрости во многих культурах?": ["Сова", "Лев", "Орел", "Волк"],
             'Кто был первым человеком, ступившим на Луну?': ["Юрий Гагарин", "Нил Армстронг", "Баз Олдрин", "Джон Глен"],
             "Какая из следующих стран является самой большой по территории?": ["США", "Канада", "Китай", "Индия"]}"""

questions = {"question": ["Кто является автором романа «Война и мир»?", "Какое животное считается символом мудрости во многих культурах?",
                          'Кто был первым человеком, ступившим на Луну?', "Какая из следующих стран является самой большой по территории?"],
            'answer1': ["Федор Достоевксий", "Лев Толстой", "Александр Солжнецын", "Антон Чехов"], 
             "answer2": ["Сова", "Лев", "Орел", "Волк"],
             'answer3': ["Юрий Гагарин", "Нил Армстронг", "Баз Олдрин", "Джон Глен"],
             "answer4": ["США", "Канада", "Китай", "Индия"]}

answers = [["Федор Достоевксий", "Лев Толстой", "Александр Солжнецын", "Антон Чехов"],
           ["Сова", "Лев", "Орел", "Волк"],
           ["Юрий Гагарин", "Нил Армстронг", "Баз Олдрин", "Джон Глен"],
           ["США", "Канада", "Китай", "Индия"]]


@bot.message_handler(commands=['start'])
def start(message):

    city = {'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'],
        'Год основания': [1147, 1703, 1893, 1723], 
        'Население': [11.9, 4.9, 1.5, 1.4]} #Создаём словарь с нужной информацией о городах.
 
    #df = pd.DataFrame(questions)
    #df.to_csv('D:/nur_bot/who_are_you_without_your_bot/Questions.csv', index = False) 
    
    #df = pd.read_csv('D:/nur_bot/who_are_you_without_your_bot/GfG.csv')
    
    #df = pd.read_csv('D:/nur_bot/who_are_you_without_your_bot/Questions.csv')

    #print(df.answer1)
    first_mess = "Привет!"
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, first_mess, reply_markup=markup)
    second_mess="Тебе придется ответить на следующие вопросы 😁"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("ОК")
    markup.add(btn1)
    bot.send_message(message.chat.id, second_mess, reply_markup=markup)
    

@bot.message_handler(content_types=['text'])

def question(message):

    if (message.text=="ОК"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("next", callback_data='next'))
        """for num, ans in enumerate(answers):
          markup.row(types.InlineKeyboardButton(ans))
          ans=answers[num]
          markup.add(types.KeyboardButton(ans[0]))
          markup.add(types.InlineKeyboardButton(ans[1]))
          markup.add(types.InlineKeyboardButton(ans[2]))
          markup.add(types.InlineKeyboardButton(ans[3]))
          question_msg=f"{num+1}. {question}"
          bot.send_message(message.chat.id, question_msg, reply_markup=markup)
          bot.register_callback_query_handler(message, statistics)"""

        bot.send_message(message.chat.id, text='Tap, please', reply_markup=markup)

@bot.callback_query_handler(func=lambda query: True)
def handler(query):
    if (query.data =="next"):
        #markup=types.InlineKeyboardButton()
        #markup.add(types.InlineKeyboardButton("done", callback_data="done"))
        bot.edit_message_text(text='tnx', chat_id=query.message.chat.id, message_id=query.message.id, reply_markup=None)

import csv
import datetime
import os
import pandas as pd
import time

def statistics(message):
   user_id=message.user_id
   answer=message.text
   bot.send_message(message.chat_id, text="hi")
   time.sleep(50000)
   """df = pd.read_csv('test.csv', names=['data','user_id','answer'])
   print(pd)
   data = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M")
   with open('test.csv', 'a', newline="", encoding='UTF-8') as fil:
        wr = csv.writer(fil, delimiter=',')
        wr.writerow([data, user_id, answer])"""
   

bot.polling(non_stop=True)