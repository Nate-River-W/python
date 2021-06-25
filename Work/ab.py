import telebot
import time

bot = telebot.TeleBot('1221440480:AAGBWJjnH6XlUvXgiQCRsx3mlZjyq6BfPTg')


@bot.message_handler(content_types=['text'])
def test(message):
    for i in range(500):
        bot.send_message(message.chat.id, 'text')
        time.sleep(5)

bot.polling(none_stop=True)