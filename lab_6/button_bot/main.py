import telebot
import config
import parse

from telebot import types

date = ''

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Сегодня")
    item2 = types.KeyboardButton("На пять дней")

    markup.add(item1, item2)

    bot.send_message(message.from_user.id, "Данный бот умеет предсказывать погоду !!!\nЧтобы узнать его функционал введите /help", reply_markup=markup)


@bot.message_handler(commands=['help'])
def info(message):
    bot.send_message(message.from_user.id, "Чтобы узнать погоду на сегодня: нажмите на кнопку \"сегодня\"\nЧтобы узнать погоду на 5 дней: нажмите на кнопку \"На пять дней\"")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global date
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Чтобы узнать прогноз погоды введите дату в формате: \{dd.mm.yyyy\}")
    elif (message.chat.type == 'private'):
        if (message.text == 'Сегодня'):
            bot.send_message(message.from_user.id, parse.Get_Weather_Today())
        elif (message.text == 'На пять дней'):
            bot.send_message(message.from_user.id, parse.Get_Weather_Five_Day())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=2)



