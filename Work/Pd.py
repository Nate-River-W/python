import json
import requests

data = {
'binIin': "131140025304",
'catalogId': 3345,
'email': "nico.96@mail.ru",
'isUseRecommendPo': False,
'name': "Тест не звонить",
'phone': "77075553518",
'productGroupDivision': "2",
'registrationCheckbox': False,
'serverId': 1

}


r = requests.post('https://integration.ismet.kz/bpmn/api/v2/public/potentialDeal/mobile', json=data)
r = r.json()

a = input('sms code:  ')
data2 = {

     'type': 'potentialDeal',
     'emailOrPhone': 77075553518,
     'code': a,
     'email': 'nico.96@mail.ru'

}
r2 = requests.post('https://integration.ismet.kz/bpmn/api/v1/public/accountRecover/verifyCode', json=data2)

r2 = r2.json()
r2 = r2['header']

data3 = {

  "id": r['id'],
  "token": r2['errorText'],
  "phone": "77075553518"


}
r3 = requests.post("https://integration.ismet.kz/bpmn/api/v2/public/potentialDeal/submit", json=data3)

print(r3.json())