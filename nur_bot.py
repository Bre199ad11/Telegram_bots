
# -*- coding: utf-8 -*-
import telebot
from telebot import types # для указание типов
import time
#import telegram
#import aiogram
#from aiogram import types




bot = telebot.TeleBot('6375057076:AAGfhVl06PyjhJddaxJt-eTWEr3YDJQhxo8')

@bot.message_handler(commands=['start'])

def start(message):
    statistics_write(message.chat.id,message.text)
    first_mess = "Привет!"
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, first_mess, reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("⚡️Купить билеты ")
    btn2 = types.KeyboardButton("ℹ️ Информация о фестивале")
    btn5 = types.KeyboardButton("📍Локации фестиваля")
    btn4 = types.KeyboardButton("💚Художники")
    btn3 = types.KeyboardButton("🟢Мы в соцсетях")
    btn6 = types.KeyboardButton("❓F.A.Q.")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text = '⚡️Купить билеты', callback_data='⚡️Купить билеты')
    button2 = types.InlineKeyboardButton(text = 'ℹ️ Информация о фестивале', callback_data='ℹ️ Информация о фестивале')
    button3 = types.InlineKeyboardButton(text = '📍Локации фестиваля', callback_data='📍Локации фестиваля')
    button4 = types.InlineKeyboardButton(text = '💚Художники', callback_data='💚Художники')
    button5 = types.InlineKeyboardButton(text = '🟢Мы в соцсетях', callback_data='🟢Мы в соцсетях')
    button6 = types.InlineKeyboardButton(text = '❓F.A.Q.', callback_data='❓F.A.Q.')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, text="В меню можете выбрать то, что вас интересует", reply_markup=markup)
  


@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     """if function_call.data == "yes":
        second_mess = "Международный фестиваль медиаискусства NUR состоится в Казани с 8 по 10 сентября \n\nЧто такое NUR? NUR - это\n— инсталляции\n— выставки цифрового искусства\n— аудиовизуальные перформансы\n— лекции\n— ночная программа\n\nА больше о фестивале ты можешь узнать на нашем сайте 👇"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://nurfestival.com/"))
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        bot.answer_callback_query(function_call.id)
        #time.sleep(1)
        markup = types.InlineKeyboardMarkup()
        third_mess="Также ты можешь принять участие в фестивале в роли волонтера 🤗\nДля этого тебе нужно заполнить гугл форму"
        markup.add(types.InlineKeyboardButton("Заполнить форму", url="https://forms.gle/XjUFbEUnEcdXs9peA"))
        bot.send_message(function_call.message.chat.id, third_mess, reply_markup=markup)
        #bot.answer_callback_query(function_call.id)"""
     
     if (function_call.data == "⚡️Купить билеты"):
        statistics_write(function_call.message.chat.id,function_call.message.text)
        markup = types.InlineKeyboardMarkup()
        send_msg="Купить билеты можно здесь 👇"
        markup.add(types.InlineKeyboardButton("Купить билеты", url="https://60b2ada915419520bedc5fd8.ticketscloud.org/"))
        bot.send_message(function_call.message.chat.id, send_msg, reply_markup=markup)

     elif (function_call.data == "❓F.A.Q."):
        statistics_write(function_call.message.chat.id,function_call.message.text)
        markup = types.InlineKeyboardMarkup()
        msg="""Ответы на часто задаваемые вопросы собрали в нашей группе Вконтакте 💚"""
        markup.add(types.InlineKeyboardButton("❓F.A.Q.", url="https://vk.com/@nur.festival-nur-2023-faq"))
        bot.send_message(function_call.message.chat.id, msg, reply_markup=markup, parse_mode="Markdown")

     elif (function_call.data == "📍Локации фестиваля"):
        statistics_write(function_call.message.chat.id,function_call.message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn0=types.KeyboardButton("Платные локации")
        btn1=types.KeyboardButton("Ночная программа")
        btn2=types.KeyboardButton("Открытие фестиваля")
        btn3=types.KeyboardButton("Образовательная программа")
        btn4=types.KeyboardButton("Бесплатные локации")
        btn5=types.KeyboardButton("Где купить мерч")
        btn6=types.KeyboardButton("Показать все локации")
        btn7=types.KeyboardButton("Список локаций в 2ГИС")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, btn4, btn1, btn5, btn2, btn6, btn3, btn7, back)
        bot.send_message(function_call.message.chat.id, text="Какие локации вас интересуют?", reply_markup=markup)

     elif (function_call.data == "ℹ️ Информация о фестивале"):
      statistics_write(function_call.message.chat.id,function_call.message.text)
      markup = types.InlineKeyboardMarkup()
      msg="""*Международный фестиваль медиаискусства NUR*
_7, 8-10 сентября_
Казань \n
*7 сентября*
_Открытие фестиваля NUR х Savin Premier_
Эрика Лундмоен, Никола Мельников, инсталляция от Radugadesign
Квартал Savin City, ул. Алексея Козина, 2
[Вход свободный, по регистрации](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/64e7bb81b8b68bbb761cdef8?partner_id=60b2ada915419520bedc5fd8) 
0+

*8-10 сентября*
_Основная программа фестиваля_
Более 10 локаций по всей Казани
Инсталляции от ведущих студий и художников из России, Японии, Мексики и Канады
Маппинг-шоу на Спасской башне Кремля
[Билеты, информация о художниках и локациях](https://nurfestival.com/program/)
0+

_Образовательная программа_
12 лекций и дискуссий от художников, кураторов фестивалей, креативных продюсеров и других лидеров индустрии \n Национальная библиотека РТ, ул. Пушкина, 86 \n
[Регистрация и расписаниe](https://nurfestival.com/edu/)

*9 сентября*
_Ночная программа NUR NIGHT_
16 артистов, 2 сцены под трибунами Ак Барс Арены
Ак Барс Арена, просп. Ямашева, 115 А, сектор B, вход VSA 1
[Билеты и лайнап](https://nurfestival.com/nurnight2023/)
18+"""
      markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://nurfestival.com/"))
      bot.send_message(function_call.message.chat.id, msg, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)

     elif (function_call.data == "💚Художники"):
      statistics_write(function_call.message.chat.id,function_call.message.text)
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
      btn1=types.KeyboardButton("Посмотреть всех художников")
      btn2=types.KeyboardButton("Tatsuru Arai")
      btn3=types.KeyboardButton("Broken Composers")
      btn4=types.KeyboardButton("Robohall")
      btn5=types.KeyboardButton("Formate")
      btn6=types.KeyboardButton("Ali Phi")
      msg= "Какой художник вас интересует?"
      back = types.KeyboardButton("Вернуться в главное меню")
      markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
      bot.send_message(function_call.message.chat.id, msg, reply_markup=markup)

     elif (function_call.data == "🟢Мы в соцсетях"):
      statistics_write(function_call.message.chat.id,function_call.message.text)
      send_msg="Социальные сети фестиваля NUR 💚 \n \n [⚡️ Instagram](https://instagram.com/nur.festival) \n \n [⚡️ Telegram](https://t.me/nurfestival) \n \n [⚡️ VK](http://vk.com/nur.festival)"
      markup = types.InlineKeyboardMarkup()
      bot.send_message(function_call.message.chat.id, send_msg, reply_markup=markup, parse_mode="MarkdownV2")
    
     elif function_call.data=="back":
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
      button1 = types.KeyboardButton("⚡️Купить билеты")
      button2 = types.KeyboardButton("ℹ️ Информация о фестивале")
      btn3 = types.KeyboardButton("📍Локации фестиваля")
      btn4 = types.KeyboardButton("💚Художники")
      btn5 = types.KeyboardButton("🟢Мы в соцсетях")
      markup.add(button1, button2, btn3, btn4, btn5)
      bot.send_message(function_call.message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

     
        
@bot.message_handler(content_types=['text'])

def func(message):
    
    if(message.text == "⚡️Купить билеты"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      send_msg="Купить билеты можно здесь 👇"
      markup.add(types.InlineKeyboardButton("Купить билеты", url="https://60b2ada915419520bedc5fd8.ticketscloud.org/"))
      bot.send_message(message.chat.id, send_msg, reply_markup=markup)

    elif (message.text=="📍Локации фестиваля"):
      statistics_write(message.chat.id,message.text)
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
      btn0=types.KeyboardButton("Платные локации")
      btn1=types.KeyboardButton("Ночная программа")
      btn2=types.KeyboardButton("Открытие фестиваля")
      btn3=types.KeyboardButton("Образовательная программа")
      btn4=types.KeyboardButton("Бесплатные локации")
      btn5=types.KeyboardButton("Где купить мерч")
      btn6=types.KeyboardButton("Показать все локации")
      btn7=types.KeyboardButton("Список локаций в 2ГИС")
      back = types.KeyboardButton("Вернуться в главное меню")
      markup.add(btn0, btn4, btn1, btn5, btn2, btn6, btn3, btn7, back)
      bot.send_message(message.chat.id, text="Какие локации вас интересуют?", reply_markup=markup)
    
    elif (message.text=="Платные локации"):
      """btn1=types.KeyboardButton("Дом типографии Каримовых")
      btn2=types.KeyboardButton("Artplay Media")
      btn3=types.KeyboardButton("Городской магистрат")
      statistics_write(message.chat.id,message.text)
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
      back = types.KeyboardButton("Вернуться в главное меню")
      #markup.add(btn1, btn2, btn3, btn4, btn5, btn7, btn8, back)"""
      msg="""*Локация 1* 
_Дом типографии Каримовых_
ул. Парижской Коммуны, 20/37
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8) 

media.tribe — INTERSECTION

*Локация 2* 
_Artplay Media_
ул. Пушкина, 17
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8) 

Tatsuru Arai — Face Of Universe
ALI PHI — ENFE'AL
Rus Khasanov  — Нур 

*Локация 3*
_Городской магистрат_
ул. Баумана, 3
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8) 

Sila Sveta — Newton

*Локация 4*
_Цирк_
Площадь Тысячелетия, 2
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8) 

Formate — Boz

*Локация 8*
_Ангар Технополис-КАИ_
ул.Подлужная, 57 
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8)

Robohall — Теплица

*Локация 9*
_Экстрим-парк «УРАМ»_
Кремлевская наб., 33
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8)

Broken Composers — Laser meadows
F3 — Eje Sentido

*Локация 11* 
_Завод Александрова_
ул. Габдуллы Тукая,97Б
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8)

Panterra — Terminal"""
      markup = types.InlineKeyboardMarkup()
      bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)

    elif (message.text=="Открытие фестиваля"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      msg="""ОТКРЫТИЕ ФЕСТИВАЛЯ 

*7 сентября *
_Открытие фестиваля NUR х Savin Premier_
Эрика Лундмоен, Никола Мельников, инсталляция от Radugadesign
Квартал Savin City, ул. Алексея Козина, 2
[Вход свободный, по регистрации](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/64e7bb81b8b68bbb761cdef8?partner_id=60b2ada915419520bedc5fd8)
0+"""
      bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)

    elif (message.text=="Образовательная программа"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      msg="""ОБРАЗОВАТЕЛЬНАЯ ПРОГРАММА

*8—10 сентября*
_Образовательная программа_
12 лекций и дискуссий от художников, кураторов фестивалей, креативных продюсеров и других лидеров индустрии
Национальная библиотека РТ, ул. Пушкина, 86 
[Регистрация и расписание](https://nurfestival.com/edu/)
0+"""
      bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)

    elif (message.text=="Бесплатные локации"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      msg="""БЕСПЛАТНЫЕ ЛОКАЦИИ 

*Локация 5*
_Спасская башня_
ул. Шейнкмана, 8
Время работы: 19.00—22.00
Вход свободный 

Маппинг НУР х Тинькофф 
kiselevisual & morotape
MOTOREFISICO
Electroartel
RODAR STUDIO
ILLUMINARIUM3000

*Локация 6*
_парк Черное озеро_
центральная клумба
Время работы: 19.00—22.00
Вход свободный 

[Splaces.studio](https://Splaces.studio) — Nidum

*Локация 7*
_Национальная библиотека РТ_
ул. Пушкина, 86
Время работы: 12.00—21.00

Образовательная программа фестиваля 
12.00—16.00 
[Вход свободный, по регистрации](https://nurfestival.com/edu/) 

Шоукейс Простор x Generative Gallery
16.00—21.00
Вход свободный

*Локация 10* 
_Квартал Savin City_
ул. Алексея Козина, 2

*7 сентября*
_Открытие фестиваля NUR х Savin Premier_ 
Эрика Лундмоен, Никола Мельников, инсталляция от Radugadesign
Квартал Savin City, ул. Алексея Козина, 2
[Вход свободный, по регистрации](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/64e7bb81b8b68bbb761cdef8?partner_id=60b2ada915419520bedc5fd8) 

*8—10 сентября*
Время работы: 19.00—22.00
Вход свободный 

Radugadesign — B#ffffff"""
      bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)
      #time.sleep(100)
    
    elif (message.text=="Где купить мерч"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      msg="""МЕРЧ 

💚* Мерч можно приобрести в дни фестиваля (8—10 сентября) на 4 локациях:*

• Национальная библиотека РТ (ул. Пушкина, 86)
• Artplay Media (ул. Пушкина, 17)
• Цирк (Площадь Тысячелетия, 2)
• Дом типографии Каримовых (ул. Парижской Коммуны, 20/37)
"""
      bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown")
    
    elif (message.text=="Показать все локации"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      msg="""ВСЕ ЛОКАЦИИ 

*Локация 1*
_Дом типографии Каримовых_
ул. Парижской Коммуны, 20/37
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8) 

media.tribe — INTERSECTION

*Локация 2* 
_Artplay Media_
ул. Пушкина, 17
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8) 

Tatsuru Arai — Face Of Universe
ALI PHI — ENFE'AL
Rus Khasanov  — Нур 

*Локация 3*
_Городской магистрат_
ул. Баумана, 3
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8) 

Sila Sveta — Newton

*Локация 4* 
_Цирк_
Площадь Тысячелетия, 2
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8) 

Formate — Boz

*Локация 5* 
_Спасская башня_
ул. Шейнкмана, 8
Время работы: 19.00—22.00
Вход свободный 

Маппинг НУР х Тинькофф 
kiselevisual & morotape
MOTOREFISICO
Electroartel
RODAR STUDIO
ILLUMINARIUM3000

*Локация 6*
_парк Черное озеро_
центральная клумба
Время работы: 19.00—22.00
Вход свободный 

[Splaces.studio](https://Splaces.studio) — Nidum

*Локация 7*
_Национальная библиотека РТ_
ул. Пушкина, 86
Время работы: 12.00—21.00

_Образовательная программа фестиваля_
12.00—16.00 
[Вход свободный, по регистрации](https://nurfestival.com/edu/) 
Шоукейс Простор x Generative Gallery
16.00—21.00
Вход свободный

*Локация 8* 
_Ангар Технополис-КАИ_
ул.Подлужная, 57 
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8)

Robohall — Теплица

*Локация 9* 
_Экстрим-парк «УРАМ»_
Кремлевская наб., 33
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8)

Broken Composers — Laser meadows
F3 — Eje Sentido

*Локация 10*
_Квартал Savin City_ 
ул. Алексея Козина, 2

*7 сентября* 
_Открытие фестиваля NUR х Savin Premier_ 
Эрика Лундмоен, Никола Мельников, инсталляция от Radugadesign
Квартал Savin City, ул. Алексея Козина, 2
[Вход свободный, по регистрации](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/64e7bb81b8b68bbb761cdef8?partner_id=60b2ada915419520bedc5fd8) 

*8—10 сентября*
Время работы: 19.00—22.00
Вход свободный 

Radugadesign — B#ffffff

*Локация 11*
_Завод Александрова_
ул. Габдуллы Тукая,97Б
Время работы: 16.00—23.00
[Вход по билету](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/63ff8b9fe4ef09c522f9c8e7?partner_id=60b2ada915419520bedc5fd8)
Panterra — Terminal"""
      bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)
      
    elif (message.text=="Список локаций в 2ГИС"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      msg="""Для удобной навигации по локациям в дни фестиваля можно будет воспользоваться сервисом 2ГИС 💚"""
      markup.add(types.InlineKeyboardButton("Перейти в 2ГИС", url="https://go.2gis.com/c3ww0v"))

      bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown")

      """elif (message.text=="Национальная библиотека РТ"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url_location1="https://sun9-18.userapi.com/impg/jYPwSmNqrjpyaL-muU-jhzxaw0swUonvqW-vmw/hB91wJKUPvQ.jpg?size=2560x2560&quality=95&sign=4fd6c5397094334762b750efb918299a&type=album"
      url_location1_1="https://sun9-73.userapi.com/impg/2jBKkiusn2x1GTcM1GTERBvuPDDfvOzNR6_gtQ/iHM5CvLKQz8.jpg?size=2560x2560&quality=95&sign=c7533ccee3ee26ea017f0779098dd98c&type=album"
      caption1=("Традиционно штабом «НУРа» станет Национальная библиотека Республики Татарстан — величественное здание в центре Казани. \nКогда-то здесь находился ленинский мемориал, но в 2020 году комплекс пережил масштабные изменения и стал современным общественным пространством.\n\n"+
                "В дни фестиваля Национальная библиотека будет выполнять несколько функций:\n\n"+
                "✅ Образовательный центр, где состоятся бесплатные лекции и дискуссии при участии артистов и лидеров индустрии. Расписание и ссылки на регистрацию мы опубликуем позже.\n\n"+
                "✅ Площадка маркета НУР, где вы сможете приобрести билеты на фестиваль и наш мерч.\n\n"+
                "✅ Центр аккредитации, где артисты и представители прессы могут получить специальные бейджи и получить необходимую информацию.")
      markup.add(types.InlineKeyboardButton("Показать локацию в картах", url="https://yandex.ru/maps/-/CPfyNdR"))
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(url_location1, caption1),telebot.types.InputMediaPhoto(url_location1_1)])
      bot.send_message(message.chat.id, text="Ссылка на локацию 🗺️", reply_markup=markup)
                                            
    elif (message.text=="Парк «Черное озеро»"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url_location1="https://sun9-2.userapi.com/impg/ppo-KqnB8TTMyP_Qj9EOoR3ijHz17bEd_KcfdQ/xm-ItY8WDmo.jpg?size=2560x2560&quality=95&sign=1690d6a5e975c4e0386a71bb232a6c0a&type=album"
      url_location1_1="https://sun9-47.userapi.com/impg/xYbEIBF2V5MZuBt0SQzsZhOQkb4cZ1aVErwLiA/RlH05fq4d0E.jpg?size=2560x2560&quality=95&sign=b845f9d54495ee3ad233d59a3c76fc79&type=album"
      caption1=("Парк «Черное озеро» — один из старейших в Казани.\n\n"+
                "Парк получил название благодаря одноименному озеру, которое решили благоустроить в 1829 году. К концу века водоем стал зарастать водорослями и городские власти его засыпали, но позже он был возрожден. В советское время зимой заливали каток, и благодаря этому событию в Казани появилась своя хоккейная команда.\n\n"+
                "В 2021 году на Черном озере завершился последний этап очередного благоустройства. Этим занималось московское архитектурное бюро Wowhaus, которое создавало проекты для парка Горького в Москве, Крымской набережной и института «Стрелка». В том числе они обновили символ парка — Арку Влюбленных. Ее акустический эффект позволяет общаться шепотом, располагаясь друг напротив друга лицом к стене, и отчетливо слышать собеседника.")
      markup.add(types.InlineKeyboardButton("Показать локацию в картах", url="https://yandex.ru/maps/-/CTC~Zpb"))
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(url_location1, caption1),telebot.types.InputMediaPhoto(url_location1_1)])
      bot.send_message(message.chat.id, text="Ссылка на локацию 🗺️", reply_markup=markup)


    elif (message.text=="Экстрим-парк «УРАМ»"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url_location1="https://sun9-12.userapi.com/impg/btaUyhv5AFikOPI9nMYnAIs_suo6zGXvXr0ssQ/b44SRX19ZvM.jpg?size=2560x2560&quality=95&sign=4584064343c70df881fccbd28931e728&type=album"
      url_location1_1="https://sun9-1.userapi.com/impg/lw_SKAPA9hXdpeWB-MTZZicOysA0vGWq3hYO0A/3a1qNllYdoM.jpg?size=2560x2560&quality=95&sign=9e3ba89d6ba33865e34804e0acad9b76&type=album"
      caption1=("Еще одна локация фестиваля НУР в этом году — самый большой экстрим-парк в России «УРАМ»\n\n"+
                "Крытая часть парка появилась осенью 2021 года. Над проектом работал консорциум компании Legato Sports Architecture и бюро KOSMOS — второе может быть знакомо вам, например, по спортивному центру Nike и павильону для музея «Гараж» в Парке Горького.\n\n"+
                "Одна из инсталляций в основной программе разместится в огромном эйр-парке — уникальном объекте деревянной спортивной архитектуры и обладателе премии Архиwood-2021. Из-за волн, которые создают рельефы фигур, эту зону называют фанерным морем. Ежедневно здесь тренируются начинающие спортсмены и приезжают оттачивать навыки профессионалы высочайшего уровня.")
      markup.add(types.InlineKeyboardButton("Показать локацию в картах", url="https://yandex.ru/maps/-/CTGEzyr"))
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(url_location1, caption1),telebot.types.InputMediaPhoto(url_location1_1)])
      bot.send_message(message.chat.id, text="Ссылка на локацию 🗺️", reply_markup=markup)


    elif (message.text=="Artplay Media"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url_location1="https://sun9-14.userapi.com/impg/F71fHTxWVDtDk8MBXyfAU2gytGfEXXkXAjhrlQ/oxAm56Rw_ns.jpg?size=2560x2560&quality=95&sign=82e98efb84d0ef0eea0e9a553b1bc476&type=album"
      url_location1_1="https://sun9-68.userapi.com/impg/r4JdF8Np8J_koCuoOlIt2r0STlPfLQjycsncrw/x3tRpOeXxOU.jpg?size=2560x2560&quality=95&sign=886448bde3b835f878dc8330ec40fca6&type=album"
      caption1=("Уникальный центр цифрового искусства открылся в Казани этой весной и уже стал заметной точкой на культурной карте города. Здесь проходят мультимедийные выставки в жанре edutainment (education+entertainment — образование и развлечение), разработанные на стыке цифровых технологий и кинематографа, а также театральные, музыкальные и пластические перформансы.\n\n"+ 
                "20 одновременно работающих проекторов, объемный звук и угол обзора 360 градусов позволяют зрителям полностью погрузиться в художественные произведения так, что эмоции от контента захватят вас с головой. Зрители премьеры перформанса PENTA, который проходил в Artplay Media в июне, наверняка это подтвердят!")
      markup.add(types.InlineKeyboardButton("Показать локацию в картах", url="https://yandex.ru/profile/-/C-EHQuD"))
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(url_location1, caption1),telebot.types.InputMediaPhoto(url_location1_1)])
      bot.send_message(message.chat.id, text="Ссылка на локацию 🗺️", reply_markup=markup)"""
    
    elif (message.text=="Ночная программа"):
      #time.sleep(3000)
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      """url_location1="https://t.me/nurfestival/393"
      #url_location1_1="https://sun9-68.userapi.com/impg/r4JdF8Np8J_koCuoOlIt2r0STlPfLQjycsncrw/x3tRpOeXxOU.jpg?size=2560x2560&quality=95&sign=886448bde3b835f878dc8330ec40fca6&type=album"
      caption1=("Расскрываем тайнy локации: ночная программа фестиваля пройдет в здании бывшего управления завода «Теплоприбор»!\n\n"+
                "Здание уникально тем, что возводилось во времена, когда масштаб и размах приветствовался во всем: отсюда высокие потолки и большие оконные проемы, просторные холлы и широкие лестницы.\n\n"+
                "Скоро из типовой советской постройки оно превратится в современное бизнес-пространство в индустриальном стиле. И NUR NIGHT — это единственная возможность незабываемо провести ночь на «Теплоприборе»💥\n\n"+
                "Билеты по ссылке: nurfestival.com")
      markup.add(types.InlineKeyboardButton("Показать локацию в картах", url="https://yandex.ru/profile/-/C-rgapa"))"""
      #bot.send_media_group(message.chat.id, [telebot.types.InputMediaVideo(url_location1, caption=caption1)])
      msg="""НОЧНАЯ ПРОГРАММА

*9 сентября*
_Ночная программа NUR NIGHT_ 
16 артистов, 2 сцены под трибунами Ак Барс Арены  
Ак Барс Арена, просп. Ямашева, 115 А, сектор B, вход VSA 1
[Билеты и лайнап](https://nurfestival.com/nurnight2023/)
18+"""
      bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)

    elif(message.text == "ℹ️ Информация о фестивале"):
        statistics_write(message.chat.id,message.text)
        markup = types.InlineKeyboardMarkup()
        msg="""*Международный фестиваль медиаискусства NUR*
_7, 8-10 сентября_
Казань \n
*7 сентября*
_Открытие фестиваля NUR х Savin Premier_
Эрика Лундмоен, Никола Мельников, инсталляция от Radugadesign
Квартал Savin City, ул. Алексея Козина, 2
[Вход свободный, по регистрации](https://60b2ada915419520bedc5fd8.ticketscloud.org/e/64e7bb81b8b68bbb761cdef8?partner_id=60b2ada915419520bedc5fd8) 
0+

*8-10 сентября*
_Основная программа фестиваля_
Более 10 локаций по всей Казани
Инсталляции от ведущих студий и художников из России, Японии, Мексики и Канады
Маппинг-шоу на Спасской башне Кремля
[Билеты, информация о художниках и локациях](https://nurfestival.com/program/)
0+

_Образовательная программа_
12 лекций и дискуссий от художников, кураторов фестивалей, креативных продюсеров и других лидеров индустрии \n Национальная библиотека РТ, ул. Пушкина, 86 \n
[Регистрация и расписаниe](https://nurfestival.com/edu/)

*9 сентября*
_Ночная программа NUR NIGHT_
16 артистов, 2 сцены под трибунами Ак Барс Арены
Ак Барс Арена, просп. Ямашева, 115 А, сектор B, вход VSA 1
[Билеты и лайнап](https://nurfestival.com/nurnight2023/)
18+"""
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://nurfestival.com/"))
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown", disable_web_page_preview=True)
    
    elif(message.text=="💚Художники"):
        statistics_write(message.chat.id,message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1=types.KeyboardButton("Посмотреть всех художников")
        btn2=types.KeyboardButton("Tatsuru Arai")
        btn3=types.KeyboardButton("Broken Composers")
        btn4=types.KeyboardButton("Robohall")
        btn5=types.KeyboardButton("Formate")
        btn6=types.KeyboardButton("Ali Phi")
        msg= "Какой художник вас интересует?"
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, msg, reply_markup=markup)

    elif(message.text=="Посмотреть всех художников"):
        statistics_write(message.chat.id,message.text)
        markup = types.InlineKeyboardMarkup()
        msg="""Ознакомиться со всеми художниками и их локациями можно на сайте фестиваля 💚"""
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://nurfestival.com/"))
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown")
    
    elif (message.text=="Tatsuru Arai"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url="https://t.me/nurfestival/355"
      caption1=("Tatsuru Arai — выпускник Токийского музыкального колледжа и Музыкальной академии Ханса Эйслера в Берлине, ученик знаменитых композиторов Акиры Нисимуры, Тосио Хосокавы, Бернарда Ланга и Вольфганга Хайнигера. С 2016 года японский артист сочиняет Hyper Serial Music — алгоритмическую музыку, созданную с помощью самых современных технологий, включая искусственный интеллект.\n\n"+
                "На одной из локаций фестиваля он представит работу Face Of Universe.\n\n"+
                "Ключевую роль в ней играют растения как часть земной экосистемы солнечного происхождения. Согласно статьям на основе наблюдений NASA, их количество растет благодаря поглощению углекислого газа, выделяемого людьми, и одновременно с этим они способны влиять на экологию урбанизированных территорий. В инсталляций форма сеульских цветов воспроизводится с помощью алгоритма, а изображения и музыка генерируются посредством ИИ — будто бы клетки цветка являются частью космической формы жизни.")
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaVideo(url, caption=caption1)])
    
    elif (message.text=="Andreii Luch"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url="https://t.me/nurfestival/361"
      caption1=("Андрей Луч — медиахудожник и креативный директор студии LUCH, изучающий неочевидные пересечения науки и сознания человека. Вклад студии в художественный ландшафт включает архитектурные медиаинсталляции для таких пространств Москвы, как Supermetall и Дизайн-завод (Flacon), а также участие в фестивалях НУР прошлых лет, SIGNAL и «ПРОСВЕТ».\n\n"+
                "На фестивале НУР в этом году автор представляет инсталляцию "+ "Ψ1 / Ψ2,"+" которая позволяет исследовать идею связи между сознанием и квантовой механикой. Саунд для нее напишет @nomusicians")
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaVideo(url, caption=caption1)])

    elif (message.text=="Broken Composers"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url="https://t.me/nurfestival/366"
      caption1=("Третий участник основной программы фестиваля НУР — Broken Composers.\n\n"+
                "Дуэт междисциплинарных художников Кирилла Рейва и Виталия Юртаева с 2017 года занимается медиаискусством, иммерсивными инсталляциями, экспериментальной музыкой и сценическими перфомансами. Их радикальный эстетический язык нацелен на искажение восприятия и попытку вырвать художников и зрителей из повседневной парадигмы.\n\n"+
                "На фестивале ваше внимание захватит пространственная инсталляция «Laser Meadows». Каждый зритель сможет пройти по склонам «долины» босиком и наблюдать, как мимо синхронно с музыкой плывут сложные абстрактные узоры Лазерной Люмии. Они разворачиваются длинными петлями и волнами без явного начала и конца, цифровых и физических рамок, пикселей и экранов — пребывание в таком пространстве погружает в медитативное состояние, позволяет унять поток мыслей в голове и ощутить единение с природой и людьми вокруг.")
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaVideo(url, caption=caption1)])

    elif (message.text=="Robohall"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url="https://t.me/nurfestival/370"
      caption1=("Следующий участник основной программы нашего фестиваля — международная студия креативного инжиниринга и робототехники Robohall.\n\n"+
                "Команду отличает работа с физическими объектами, которые приобретают качественно новые свойства благодаря синергии механики с программными разработками. За последний год студия приняла участие в нескольких десятках проектов, среди которых Формула 1 в Баку, постановки на сценах Александринского и Михайловского театров, образовательная science-art программа и арт-резиденция в рамках исследовательской экспедиции на Северный полюс.\n\n"+
                "На НУРе Robohall представит «Теплицу». Основой этой инсталляции является тяжелый промышленный робот, который поворачивается в сторону солнца и реагирует на смену времени суток, имитируя поведение живого растения. Вибрации от движения в свою очередь будут преобразовываться в аудиальное полотно, ну а если гость приложит руку к отростку, то цветок считает частоту сердцебиения и начнет пульсировать в ответ.")
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaVideo(url, caption=caption1)])

    elif (message.text=="Formate"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url="https://t.me/nurfestival/374"
      caption1=("Пятый участник фестиваля — казанская мультимедийная студия Formate.\n\n"+
                "https://vk.cc/cpRiQD\n\n"+
                "Команда реализует креативные проекты в области мультимедийного искусства и дизайна; создает инсталляции и перформансы, световые и лазерные шоу, интерактивный медиаконтент и графику. Ну а каждую осень Formate организует сам фестиваль НУР.\n\n"+
                "Инсталляция BOZ, которую вы увидите, рассматривает поле взаимодействий в обществе. Только добившись баланса и отражая внутреннее сияние, мы сможем добиться гармонии с миром. Цель авторов — вдохновить зрителя погрузиться на глубину сознания и задуматься, какие чувства, принципы, эмоции и энергию он проецирует на окружающих. В отражении зритель физически видит себя и остальных, что создает концепцию коллективного опыта.")
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaVideo(url, caption=caption1)])

    elif (message.text=="Ali Phi"):
      statistics_write(message.chat.id,message.text)
      markup = types.InlineKeyboardMarkup()
      url="https://t.me/nurfestival/383"
      caption1=("Ali Phi — художник ирано-канадского происхождения, работающий на стыке искусства, науки и технологий. С помощью инсталляций, автономных машин и перформансов он исследует основные механизмы новых медиа, технологий, взаимодействий и данных. В практике Ali Phi архитектура и пространство играют важную роль как метафорически, так и физически. Художник ищет пути взаимодействие между физическим восприятием человеческого тела и его мысленными экспериментами с пространством, чтобы спровоцировать новые образы и в искусственно созданном, и в реальном мире.\n\n"+
                "Собрание ENFE'AL основано на недавнем аудиовизуальном сеттинге под названием Maqruh, что означает не одобряемые (но и не наказуемые) действия в поле исламского права. Работа вдохновлена концепцией лиминальности и контрастами между темной атмосферой и спокойствием электронной музыки в сочетании с ближневосточными и западно-азиатскими музыкальными и визуальными мотивами, слитыми с западными технологиями цифровой обработки. ")
      bot.send_media_group(message.chat.id, [telebot.types.InputMediaVideo(url, caption=caption1)])

    elif (message.text=="/help"):
      """statistics_write(message.chat.id,message.text)
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
      btn1 = types.KeyboardButton("⚡️Купить билеты")
      btn2 = types.KeyboardButton("ℹ️ Информация о фестивале")
      btn5 = types.KeyboardButton("📍Локации фестиваля")
      btn4 = types.KeyboardButton("💚Художники")
      btn3 = types.KeyboardButton("🟢Мы в соцсетях")
      markup.add(btn1, btn2, btn3, btn4, btn5)
      markup = types.InlineKeyboardMarkup(row_width=1)
      button1 = types.InlineKeyboardButton(text = '⚡️Купить билеты', callback_data='⚡️Купить билеты')
      button2 = types.InlineKeyboardButton(text = 'ℹ️ Информация о фестивале', callback_data='ℹ️ Информация о фестивале')
      button3 = types.InlineKeyboardButton(text = '📍Локации фестиваля', callback_data='📍Локации фестиваля')
      button4 = types.InlineKeyboardButton(text = '💚Художники', callback_data='💚Художники')
      button5 = types.InlineKeyboardButton(text = '🟢Мы в соцсетях', callback_data='👨‍💻 Мы в соцсетях 👨‍💻')
      markup.add(button1, button2, button3, button4, button5)
      bot.send_message(message.chat.id, text="В меню можете выбрать то, что вас интересует", reply_markup=markup)"""
      markup = types.InlineKeyboardMarkup()
      statistics_write(message.chat.id,message.text)
      pd.set_option('display.max_colwidth',1000)
      df = pd.read_csv('data_nur_bot.csv', names=['data','id','command'])
      #df = pd.read_csv('data_nur_bot.csv')
      number_of_users = len(df['id'].unique())
      number_of_command=len(df['command'])
      msg1 = 'За всё время бота использовало: ' + str(number_of_users)+ '\n\n'
      msg2='За всё время использовано комманд: ' + str(number_of_command)+ '\n\n' + df.to_string()
      msg=msg1+msg2
      markup.add(types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back"))
      bot.send_message(message.chat.id, text="u", reply_markup=markup)
  

    elif (message.text=="🟢Мы в соцсетях"):
      statistics_write(message.chat.id,message.text)
      send_msg="Социальные сети фестиваля NUR 💚 \n \n [⚡️ Instagram](https://instagram.com/nur.festival) \n \n [⚡️ Telegram](https://t.me/nurfestival) \n \n [⚡️ VK](http://vk.com/nur.festival)"
      markup = types.InlineKeyboardMarkup()
      bot.send_message(message.chat.id, send_msg, reply_markup=markup, parse_mode="MarkdownV2", disable_web_page_preview=True)
    
    elif (message.text == "❓F.A.Q."):
        statistics_write(message.chat.id,message.text)
        markup = types.InlineKeyboardMarkup()
        msg="""Ответы на часто задаваемые вопросы собрали в нашей группе Вконтакте 💚"""
        markup.add(types.InlineKeyboardButton("❓F.A.Q.", url="https://vk.com/@nur.festival-nur-2023-faq"))
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown")

    elif (message.text == "/view stat"):
      markup = types.InlineKeyboardMarkup()
      statistics_write(message.chat.id,message.text)
      pd.set_option('display.max_colwidth',100)
      #df = pd.read_csv('data_nur_bot.csv', names=['data','id','command'])
      df = pd.read_csv('data_nur_bot.csv')
      number_of_users = len(df['id'].unique())
      number_of_command=len(df['command'])
      msg1 = 'За всё время бота использовало: ' + str(number_of_users)+ '\n\n'
      msg2='За всё время использовано комманд: ' + str(number_of_command)+ '\n\n' + df.to_string()
      msg=msg1+msg2
      markup.add(types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back"))
      bot.send_message(message.chat.id, text="u", reply_markup=markup)
 
    elif (message.text == "Вернуться в главное меню"):
        statistics_write(message.chat.id,message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("⚡️Купить билеты")
        btn2 = types.KeyboardButton("ℹ️ Информация о фестивале")
        btn5 = types.KeyboardButton("📍Локации фестиваля")
        btn4 = types.KeyboardButton("💚Художники")
        btn6=types.KeyboardButton("❓F.A.Q.")
        #markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn3 = types.KeyboardButton("🟢Мы в соцсетях")
        markup.add(btn1, btn2, btn3, btn4, btn6, btn5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
      
    else:
      markup = types.InlineKeyboardMarkup()
      send_msg="Извините, я вас не понимаю 😔, но вы всегда можете вернуться в главное меню!"
      markup.add(types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back"))
      bot.send_message(message.chat.id, send_msg, reply_markup=markup)



import csv
import datetime
import os
import pandas as pd
def statistics_write(user_id, command):
    data = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M")
    with open('data_nur_bot.csv', 'a', newline="", encoding='UTF-8') as fil:
        wr = csv.writer(fil, delimiter=',')
        wr.writerow([data, user_id, command])

def statistic_read(user_id):
    df = pd.read_csv('data_nur_bot.csv', names=['data','id','command'])
    number_of_users = len(df['id'].unique())
    message_to_user += 'За всё время бота использовало: ' + str(number_of_users)
    print(number_of_users)
    return message_to_user

try:
   bot.polling(non_stop=True, interval=2)
except Exception as e:
    print("Возникли технические неполадки. Приносим свои изменения!")