from selenium import webdriver
import json
from dataclasses import dataclass, asdict, field
from selenium.webdriver.support.color import Color

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")
driver = webdriver.Chrome('C:/Users/Nate/Desktop/Python/pytest/chromedriver.exe', options=options)

driver.get('https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vSIyMymvCGBCsQtCOFWcqQLdoKJEheGWLdKG'
           'zPNFHPH7MdLtvaAPXUwjJQeibwIYzwFZiTwCcXun6f2/pubhtml/sheet?headers=false&gid=771730809')

open('json.txt', 'w').close()

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

find_cities = driver.find_elements_by_tag_name('tr')
rl = Readylist()
temp_val = 7
n = 0
id_city = 0
for j in cities:
    ex_city = City(id_city, cities[id_city])
    for i in find_cities:
        temp = i.find_elements_by_tag_name('td')
        n += 1
        if (n >= 7) and (n <= 53):
            ex_object = Object(temp[2].text, temp[temp_val].text)
            ex_city.objects.append(ex_object.to_dict())
            if (n == 8):
                hex_color = temp[temp_val].value_of_css_property('background-color')
                ex_city.color = Color.from_string(hex_color).hex
    n = 0
    id_city += 1
    temp_val += 1
    rl.ready_list.append(ex_city)

itog = (json.dumps(rl.to_dict(), indent=2, ensure_ascii=False))
file = open('json.txt', 'a', encoding="utf-8")
file.write(itog)
file.close()
driver.quit()
print(itog)