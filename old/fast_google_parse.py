import requests
import json
from dataclasses import dataclass, asdict, field
from bs4 import BeautifulSoup as BS
import lxml

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}

url = ('https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vSIyMymvCGBCsQtCOFWcqQLdoKJEheGWLdKGzPNFHPH7MdLtvaAPXUwjJQeibwIYzwFZiTwCcXun6f2/pubhtml/sheet?headers=false&gid=771730809')

r = requests.get(url, headers=headers)   # Запрос на сайт для BS

open('json.txt', 'w').close()    # Очиста файла с JSON

# Соответствие id с названием города
# cities = {
#     0: 'г.Алматы',
#     1: 'г.Нур-Султан',
#     2: 'г.Шымкент',
#     3: 'Актюбинская область',
#     4: 'Акмолинская область',
#     5: 'Алматинская область	',
#     6: 'Атырауская область	',
#     7: 'ВКО',
#     8: 'Жамбылская область',
#     9: 'ЗКО',
#     10: 'Карагандинская область',
#     11: 'Костанайская область',
#     12: 'Кызылординская область	',
#     13: 'Мангистауская область',
#     14: 'Павлодарская область	',
#     15: 'СКО',
#     16: 'Туркестанская область',
#
#
# }

red = '#ff0000'
yellow = '#ffff00'
green = '#92d050'

cities = ['г.Алматы', 'г.Нур-Султан', 'г.Шымкент', 'Актюбинская область', 'Акмолинская область', 'Алматинская область',
  'Атырауская область', 'ВКО', 'Жамбылская область', 'ЗКО', 'Карагандинская область', 'Костанайская область', 'Кызылординская область',
  'Мангистауская область', 'Павлодарская область', 'СКО', 'Туркестанская область']


@dataclass
class Readylist:
    ready_list: list = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

@dataclass
class Object:
    name: str = ''
    val: str = ''

    def to_dict(self):
        return asdict(self)

@dataclass
class City:
    id: int = 0
    name: str = ''
    color: str = ''
    objects: list = field(default_factory=list)

    def to_dict(self):
        return asdict(self)


soup = BS(r.content, 'lxml')   # Получение контента
soup_tables = soup.find_all('tr')    # Поиск строк


rl = Readylist()
temp_val = 7    # Номер ячейки <td>
n = 0    # Счетчик ячеек
id_city = 0    # Счетчик по списку городов

for j in cities:    # Итерация по городам
    ex_city = City(id_city, cities[id_city])
    for i in soup_tables:    # итерация по списку ячеек
        temp = i.find_all('td')    # Ячейка <td>
        n += 1
        if (n >= 7) and (n <= 53):
            ex_object = Object(temp[2].text, ' '.join(temp[temp_val].text.split()))
            ex_city.objects.append(ex_object.to_dict())
            if n == 7:    # Получение цвета
                if temp[temp_val]['class'] == ['s18']:
                    ex_city.color = red
                elif temp[temp_val]['class'] == ['s19']:
                    ex_city.color = yellow
                elif temp[temp_val]['class'] == ['s20']:
                    ex_city.color = green
    n = 0
    id_city += 1
    temp_val += 1
    rl.ready_list.append(ex_city)


itog = (json.dumps(rl.to_dict(), indent=2, ensure_ascii=False))

file = open('json.txt', 'a', encoding="utf-8")
file.write(itog)
file.close()

print(itog)
