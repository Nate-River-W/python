import telebot
from telebot import types
bot = telebot.TeleBot('1221440480:AAFZQ8sq4pAtE2RYqrJi8oHcPIW79YY8Rrk')
@bot.message_handler(commands=['start'])


def welcome(message):
	#Keydoard
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn = types.KeyboardButton('')
	keyboard.add(btn)
	
	bot.send_message(message.chat.id, '', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])	

def button(message):
	if message.text == '':
		bot.send_message(message.chat.id, '')
	elif '' in message.text.lower():
		bot.send_message(message.chat.id, '')
	elif message.text.lower() == '':
		bot.send_message(message.chat.id, '')
	elif '' in message.text.lower():
		bot.send_message(message.chat.id, '')
bot.polling(none_stop=True)

#elif message.text == '/start':
		#bot.send_message(message.chat.id, 'Приветствую!', reply_markup=keyboard)