import requests

BIN = '131140025304'

data = {

    'binIin': '',
    'catalogId': 3345,
    'email': "nico.96@mail.ru",
    'isUseRecommendPo': False,
    'name': "Тест не звонить",
    'phone': "77075553518",
    'productGroupDivision': "2",
    'registrationCheckbox': False,
    'serverId': 1

}

data2 = {

    'type': 'potentialDeal',
    'emailOrPhone': 77075553518,
    'code': '',
    'email': 'nico.96@mail.ru'

}

data3 = {

    "id": '',
    "token": '',
    "phone": "77075553518"

}


def cheking_bin():
    check_bin = requests.get(f'https://www.ismet.kz/bin/ocp/publicbpms.rest/company/{BIN}/info?BPMS_VERSION=v2')
    if 'bin' in check_bin.json():
        return check_bin.json()['bin']
    else:
        return f'{check_bin.json()}\nКомпания по БИНу - {BIN}, не прошла проверку'


valid_bin = cheking_bin()


def send_deal():
    data['binIin'] = valid_bin
    potential_deal = requests.post('https://integration.ismet.kz/bpmn/api/v2/public/potentialDeal/mobile', json=data)
    potential_deal = potential_deal.json()

    return potential_deal['id']


def get_token_code():
    sms_code = input('Sms code:  ')
    data2['code'] = sms_code
    token_code = requests.post('https://integration.ismet.kz/bpmn/api/v1/public/accountRecover/verifyCode', json=data2)

    token_code = token_code.json()['header']
    token_code = token_code['errorText']
    return token_code


def get_deal_id():
    data3['id'] = send_deal()
    data3['token'] = get_token_code()
    end_id = requests.post("https://integration.ismet.kz/bpmn/api/v2/public/potentialDeal/submit", json=data3)

    print(end_id.json())


if len(valid_bin) == 12:
    get_deal_id()
else:
    print(valid_bin)
