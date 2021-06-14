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


potential_deal = requests.post('https://integration.ismet.kz/bpmn/api/v2/public/potentialDeal/mobile', json=data)
potential_deal = potential_deal.json()

sms_code = input('sms code:  ')
data2 = {

     'type': 'potentialDeal',
     'emailOrPhone': 77075553518,
     'code': sms_code,
     'email': 'nico.96@mail.ru'

}
get_token_code = requests.post('https://integration.ismet.kz/bpmn/api/v1/public/accountRecover/verifyCode', json=data2)

get_token_code = get_token_code.json()
get_token_code = get_token_code['header']

data3 = {

  "id": potential_deal['id'],
  "token": get_token_code['errorText'],
  "phone": "77075553518"


}
end_id = requests.post("https://integration.ismet.kz/bpmn/api/v2/public/potentialDeal/submit", json=data3)

print(end_id.json())