import telebot
import time

bot = telebot.TeleBot('1221440480:AAFZQ8sq4pAtE2RYqrJi8oHcPIW79YY8Rrk')


@bot.message_handler(content_types=['text'])
def test(message):
    for i in range(500):
        bot.send_message(message.chat.id, 'text')
        time.sleep(5)

bot.polling(none_stop=True)