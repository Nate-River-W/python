from bs4 import BeautifulSoup as BS
import requests
articul = input('Введите код товара: ')
linkshop = ('https://shop.kz/search/?q=')

URL = linkshop + articul

HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'accept':'*/*'}


def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r


def get_content(html):
	soup = BS(html, 'html.parser')
	items = soup.find_all('div', class_= 'bx_detail_chars_i')
	for item in items:
		chars = (item.find('span', class_='glossary-term').get_text()) + ' - ' + (item.find('dd', class_='bx_detail_chars_i_field').get_text())
		print(chars)
def parse():
	html = get_html(URL)
	if html.status_code == 200:
		get_content(html.text)
	else:
		print('Error')
parse()