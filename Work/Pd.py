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

print(r.json())