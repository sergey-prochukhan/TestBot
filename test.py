import telebot
from telebot import types

bot = telebot.TeleBot('8513847851:AAG3PzwcGTbYO25syg-vsEWtki59dVGgwl8')

@bot.message_handler(commands=['start'])
def start_message (message):
	bot.send_message(message.chat.id, "Тест бота")

bot.infinity_polling()
