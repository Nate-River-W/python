import telebot
from bs4 import BeautifulSoup as BS
import requests

bot = telebot.TeleBot('1221440480:AAFZQ8sq4pAtE2RYqrJi8oHcPIW79YY8Rrk')

linkshop = ('https://shop.kz/search/?q=')


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Привет. Введи код товара, чтобы получить характеристики')


@bot.message_handler(content_types=['text'])
def get_content(message):
    # Списки
    chars_one = []
    chars_two = []
    chars_three = []
    n = 0  # Индекс списков спарсенных данных

    # Запрос по коду товара
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'accept': '*/*'}
    url = linkshop + str(message.text)
    r = requests.get(url, headers=headers)

    # парсер
    soup = BS(r.content, 'html.parser')
    items = soup.find_all('div', class_='bx_detail_chars_i')

    # Обработка сообщения
    if str.isdigit(message.text):
        for item in items:
            chars_one.append(item.find('span', class_='glossary-term').get_text())
            chars_two.append(item.find('dd', class_='bx_detail_chars_i_field').get_text())

        for i in zip(chars_one, chars_two):
            chars_three.append(chars_one[n] + ' - ' + chars_two[n] + '\n')
            n += 1

        bot.send_message(message.chat.id, ''.join(chars_three))
        chars_one.clear()
        chars_two.clear()
        chars_three.clear()
    else:
        bot.send_message(message.chat.id, 'Неверный код товара')


bot.polling(none_stop=True)
