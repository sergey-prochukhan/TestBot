import telebot
from telebot import types

bot = telebot.TeleBot('8513847851:AAG3PzwcGTbYO25syg-vsEWtki59dVGgwl8')

@bot.message_handler(commands=['start'])
def start_message (message):
	bot.send_message(message.chat.id, "Тестовый бот для проверки системы хостинга чат ботов Bothost в связке с github")

bot.infinity_polling()
