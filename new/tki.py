import requests
import fake_useragent
# session = requests.Session()
#
user = fake_useragent.UserAgent().random
headers = {
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
#
# r = session.get('https://expw.net/ph/index.php', headers=headers)
# # s_token = session.cookies.get('JSESSIONID')
#
# data1 = {
#     'dologin': 1,
#     'username': 'nearpulsar',
#     'password': 'Nateriverisgod1996'
# }
#
#
# response = session.post("https://expw.net/ph/index.php", data=data1, headers=headers)
#
# #response1 = session.post("https://op.ismet.kz/back/zkau;jsessionid=", headers=headers)
#
# # f = open('file.html', 'w', encoding="utf-8")
# # f.write(response1.text)
# print(response.text)

data = {
    "query": "131140025304",
    "desc": False
}

session = requests.Session()
s = session.get('https://www.ismet.kz', headers=headers)
r = session.post('https://www.ismet.kz/bin/ocp/publicbpms.rest/search/company?BPMS_VERSION=v2', data=data, headers=headers)
print(r)