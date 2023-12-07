import telebot
from telebot import types # для указание типов


bot = telebot.TeleBot('6617526717:AAE5R81RbVBkE-BJhffF_EfgmC2PNVHJaYU')

@bot.message_handler(commands=['start'])

def start(message):
    first_mess = "Привет!"
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, first_mess, reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("вправо ")
    btn2 = types.KeyboardButton("влево")
    btn3 = types.KeyboardButton("вверх")
    btn4 = types.KeyboardButton("вниз")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="choose", reply_markup=markup)

@bot.message_handler(content_types=['text'])

def func(message):

    if(message.text == "вправо"):
         markup = types.InlineKeyboardMarkup()
         bot.send_message(message.chat.id, text="вправо", reply_markup=markup)

    if(message.text == "влево"):
         markup = types.InlineKeyboardMarkup()
         bot.send_message(message.chat.id, text="влево", reply_markup=markup)

    if(message.text == "вверх"):
         markup = types.InlineKeyboardMarkup()
         bot.send_message(message.chat.id, text="вверх", reply_markup=markup)

    if(message.text == "вниз"):
         markup = types.InlineKeyboardMarkup()
         bot.send_message(message.chat.id, text="вниз", reply_markup=markup)

try:
   bot.polling(non_stop=True, interval=2)
except Exception as e:
    print("Возникли технические неполадки. Приносим свои изменения!")