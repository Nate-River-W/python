import requests
import datetime
from getcode import getcode

BIN = '131140025304'

data_sendDeal = {

    'binIin': '',
    'catalogId': 3346,
    'comment': "Ismet видеонаблюдение",
    'email': "nico.96@mail.ru",
    'isUseRecommendPo': False,
    'name': "Тест не звонить",
    'phone': "77075553518",
    'productGroupDivision': "1",
    'recaptchaToken': 'text',
    'registrationCheckbox': False,
    'serverId': 1

}

data_tokenCode = {

    'type': 'potentialDeal',
    'emailOrPhone': 77075553518,
    'code': '',
    'email': 'nico.96@mail.ru'

}

data_getDealId = {

    "id": '',
    "token": '',
    "phone": "77075553518"

}

# Функция проверки бина
def cheking_bin():
    check_bin = requests.get(f'https://www.ismet.kz/bin/ocp/publicbpms.rest/company/{BIN}/info?BPMS_VERSION=v2')
    if 'bin' in check_bin.json():
        return check_bin.json()['bin']
    else:
        return f'{check_bin.json()}\nКомпания по БИНу - {BIN}, не прошла проверку'


valid_bin = cheking_bin()

# Функция получения id сделки
def send_deal():
    data_sendDeal['binIin'] = valid_bin
    potential_deal = requests.post('https://integration.ismet.kz/bpmn/api/v2/public/potentialDeal/',
                                   json=data_sendDeal)
    potential_deal = potential_deal.json()

    return potential_deal['id']

id_deal = send_deal()

# Функция подвтерждения смс-кода
def get_token_code():
    data_tokenCode['code'] = getcode(id_deal)
    token_code = requests.post('https://integration.ismet.kz/bpmn/api/v1/public/accountRecover/verifyCode',
                               json=data_tokenCode)

    token_code = token_code.json()['header']
    token_code = token_code['errorText']
    return token_code

# Функция отправки потенциальной сделки
def get_deal_id():
    data_getDealId['id'] = id_deal
    data_getDealId['token'] = get_token_code()
    end_id = requests.post("https://integration.ismet.kz/bpmn/api/v2/public/potentialDeal/submit",
                           json=data_getDealId)

    return end_id.json()

# Функция сохранения данных в файл
def save_result():
    result_test = get_deal_id()["id"]
    date = datetime.datetime.today()
    date = date.strftime('%Y-%m-%d | %H:%M:%S')
    all_deals = open('all_deals.txt', 'a')
    output = f'{date}  -  id | {result_test}\n'
    all_deals.write(output)
    return output

if __name__ == '__main__':
    if len(valid_bin) == 12:
        print(save_result())
    else:
        print(valid_bin)
