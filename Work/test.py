import requests

data_sendDeal = {

    'binIin': '',
    'catalogId': 3346,
    'comment': "Ismet видеонаблюдение",
    'email': "nico.96@mail.ru",
    'isUseRecommendPo': False,
    'name': "Тест не звонить",
    'phone': "77075553518",
    'productGroupDivision': "1",
    'registrationCheckbox': False,
    'serverId': 1

}
valid_bin = '131140025304'

def send_deal():
    data_sendDeal['binIin'] = valid_bin
    potential_deal = requests.post('https://integration.i-smet.kz/bpmn/api/v2/public/potentialDeal/',
                                   json=data_sendDeal)
    potential_deal = potential_deal.json()

    return potential_deal

print(send_deal())