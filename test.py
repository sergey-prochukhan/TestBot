import os
import telebot
from telebot import types


BOT_KEY = os.environ["TELEGRAM_BOT_TOKEN"]

bot = telebot.TeleBot(BOT_KEY)


menu = types.InlineKeyboardMarkup ()
menu.add(InlineKeyboardButton("Да, всё отлично!", callback_data("Да, всё отлично!"))
menu.add(InlineKeyboardButton('Нет', callback_data('Нет'))
menu.add(InlineKeyboardButton('Иное', callback_data('Иное'))							  

'''ansyes = types.KeyboardButton ("Да, всё отлично")
ansno = types.KeyboardButton ("Нет")
anselse = types.KeyboardButton ("Иное")
menu.add(ansyes,ansno,anselse)'''

@bot.message_handler(commands=['start'])
def start_message (message):
	bot.send_message(message.chat.id, "Тестовый бот для проверки системы хостинга чат ботов Bothost в связке с github. Для оценки работы сервиса отправьте ответ на вопрос: Видите ли вы это сообщение и меню с кнопками?", reply_markup = menu)

@bot.message_handler(content_types=['text'])
def text_messages(message):
	if message.text == "Да, всё отлично":
		bot.send_message(message.chat.id, "Отлично! Спасибо что уделили время", reply_markup=types.InlineKeyboardRemove())
		
	elif message.text == "Нет":
		bot.send_message(message.chat.id, "Опишите поподробнее, что пошло не так:"""", reply_markup=types.ReplyKeyboardRemove()""")
		bot.register_next_step_handler(message, forward)
	elif message.text == "Иное":
		bot.send_message(message.chat.id, "Расскажите поподробнее:"""", reply_markup = types.InlineKeyboardRemove()""")
		bot.register_next_step_handler(message, forward)
		
def forward(message):
	bot.forward_message(chat_id='@Test_Answer_b', from_chat_id = message.chat.id, message_id=message.id)
	bot.send_message(message.chat.id, "Спасибо, что уделили время.", reply_markup=menu)

"""def sheduler(message):
    bot.send_message(chat_id=context.job.context, text='Это сообщение отправлено с задержкой в 5 секунд')"""
	
bot.infinity_polling()

#Test
























