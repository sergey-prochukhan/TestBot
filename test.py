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

def text_messages(message)
	if message.text == "Да":
		bot.send_message(message.chat.id, "Отлично! спасибо за оценку!")
	elif message.text == "Нет":
		bot.send_message(message.chat.id, "Опишите поподробнее, что пошло не так:", reply_markup=types.ReplyKeyboardRemove())
	elif message.text == "Иное":
		bot.send_message(message.chat.id, "Расскажите поподробнее:", reply_markup = types.ReplyKeyboardRemove())

def forward(message)
	bot.forward_message(chat_id='@salebot_se', from_chat_id = message.chat.id, message_id=message.id)
	bot.send_message(message.chat.id, "Спасибо, что уделили время.", reply_markup = menu)
	
bot.infinity_polling()
