import requests
from bs4 import BeautifulSoup as BS
import urllib.request
#link = input('Введите ссылку: ')

dontworklist = []

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

r = requests.get('https://www.ismet.kz', headers=headers)

soup = BS(r.text, 'html.parser')

urles = soup.find_all('a')

ru = 'https://ismet.kz/ru'
kk = 'https://ismet.kz/kk'

list_links = []  # Список с ссылками

listtest = []  # Список без дублей

for url in urles:
    link_txt = url.get('href')  # Поиск ссылок по URL
    if type(link_txt) == str:
        if '/ru' in link_txt:
            link_txt = link_txt[23:]  # Обрез ссылки
            list_links.append(link_txt)

for i in list_links:  # Убираем повторяющиеся ссылки
    if i not in listtest:
        listtest.append(i)

list_links = listtest

for url in list_links:
    try:
        ru_code = requests.get(ru + url).status_code  # Проверка статус-кода РУ страниц
        kk_code = requests.get(kk + url).status_code  # Проверка статус-кода КЗ страниц
        print(ru + url + '   -   ' + str(ru_code))
        print(kk + url + '   -   ' + str(kk_code))
        if ru_code != 200:
            dontworklist.append(f'{ru}{url} - Ошибка {ru_code} Не работает')  # Нерабочие РУ ссылки
        elif kk_code != 200:
            dontworklist.append(f'{kk}{url} - Ошибка {kk_code} Не работает')  # Нерабочие КЗ ссылки
        else:
            pass
    except Exception:  # Обработка исключений неправильных ссылок
        dontworklist.append(f'{url} - Не работает')
print('\n*****    Cписок не работающих ссылок    ******\n')
print('\n'.join(dontworklist))