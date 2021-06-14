import requests
import fake_useragent
import json
# session = requests.Session()
#
user = fake_useragent.UserAgent().random
headers = {
     'user-agent': user
}
session = requests.Session()

r = session.get('https://op.ismet.kz/back/', headers=headers)
s_token = session.cookies.get('JSESSIONID')


url = 'https://op.ismet.kz/back/zkau;jsessionid=' + s_token


data1 = {
    'data_0': {"value":"ntgthm21yt33elfkzn","start":18},
    'data_1': {"value":"131140025304","start":12}
}
response = session.post(url, json=data1, headers=headers)

# f = open('file.html', 'w', encoding="utf-8")
# f.write(response1.text)
print(response.text)

# data = {
#     "query": "131140025304",
#     "from": 0,
#     "size": 50
# }
#
#
# r = requests.post('https://integration.ismet.kz/bpmn/api/v2/public/search/all', json=data, headers=headers)
# print(json.dumps(r.json(), indent=2, ensure_ascii=False))
