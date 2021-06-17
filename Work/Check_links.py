import requests
from bs4 import BeautifulSoup as BS

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
ru = 'https://ismet.kz/ru'
kk = 'https://ismet.kz/kk'
listtest = []  # Список без дублей
dont_work_list = []  # Cписок не работающих ссылок


def get_response():
    response = requests.get('https://www.ismet.kz/', headers=headers)
    return response


def get_links(list_urles):
    soup = BS(list_urles, 'html.parser')
    urles = soup.find_all('a')
    return urles


def get_content(content):
    list_links = []  # Список со ссылками
    for url in get_links(content):
        link_txt = url.get('href')  # Получение ссылок по URL
        if type(link_txt) == str:
            if '/ru' in link_txt:
                link_txt = link_txt[23:]  # Обрез ссылки
                list_links.append(link_txt)

    for i in list_links:  # Убираем повторяющиеся ссылки
        if i not in listtest:
            listtest.append(i)

    list_links = listtest
    return list_links


def send_requests(list_links):
    for url in get_content(list_links):
        try:
            ru_code = requests.get(ru + url).status_code  # Проверка статус-кода РУ страниц
            kk_code = requests.get(kk + url).status_code  # Проверка статус-кода КЗ страниц
            print(f'{ru}{url}     -     {str(ru_code)}')
            print(f'{kk}{url}     -     {str(kk_code)}')
            if ru_code != 200:
                dont_work_list.append(f'{ru}{url} - Ошибка {ru_code} Не работает')  # Нерабочие РУ ссылки
            if kk_code != 200:
                dont_work_list.append(f'{kk}{url} - Ошибка {kk_code} Не работает')  # Нерабочие КЗ ссылки
            else:
                pass
        except Exception:  # Обработка исключений неправильных ссылок
            dont_work_list.append(f'{url} - Не работает')
    print('\n*****    Cписок не работающих ссылок    ******\n')
    print('\n'.join(dont_work_list))


def check_links():
    response = get_response()
    send_requests(response.text)


check_links()