import telebot
from telebot import types

bot = telebot.TeleBot('8513847851:AAG3PzwcGTbYO25syg-vsEWtki59dVGgwl8')

menu = types.ReplyKeyboardMarkup (resize_keyboard=True)
ansyes = types.ReplyKeyboardButton ("Да")
ansno = types.ReplyKeyboardButton ("Нет")
anselse = types.ReplyKeyboardButton ("Иное")
menu.add(ansyes,ansno,ansyes)

@bot.message_handler(commands=['start'])
def start_message (message):
	bot.send_message(message.chat.id, "Тестовый бот для проверки системы хостинга чат ботов Bothost в связке с github. Для оценки работы сервиса отправьте ответ на вопрос: Видите ли вы это сообщение и меню с конпками?", reply_markup = menu)

bot.infinity_polling()
