import requests
import json

url = 'https://idp.ismet.kz/auth/realms/ocp/protocol/openid-connect/token'

data_for_token = {
    'client_id': 'aem_system',
    'grant_type': 'password',
    'client_secret': '0b9acb8f-8a12-4c6a-ad17-4c283215fc23',
    'username': 'aibektokmanov@yandex.kz',
    'password': 'Qwerty123'

}

data_for_callback = {

    'name': 'Тест не звонить',
    'phone': '77075553518',
    'email': 'nico.96@mail.ru',
    'serverId': 1,
    'catalogId': 3734,
    'registrationCheckbox': False

}


def get_response():
    response = requests.post(url, data=data_for_token)
    response = response.json()['access_token']
    token = {
        'Authorization': f'Bearer {response}'
        }
    return token


def send_callback():
    token = get_response()
    end_json = requests.post('https://integration.ismet.kz/bpmn/api/v2/system/kzCallBack/request',
                             json=data_for_callback,
                             headers=token)
    return end_json


print(send_callback().json())
