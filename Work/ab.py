import requests
import json

url = 'https://idp.ismet.kz/auth/realms/ocp/protocol/openid-connect/token'

data_for_token = {
    'client_id': 'aem_system',
    'grant_type': 'password',
    'client_secret': '0b9acb8f-8a12-4c6a-ad17-4c283215fc23',
    'username': 'nico.96@mail.ru',
    'password': 'Qwerty12345'

}


def get_response():
    response = requests.post(url, data=data_for_token)
    response = response.json()['access_token']
    token = {
        'Authorization': f'Bearer {response}'
        }
    return token


def test():
    info = requests.get('https://integration.ismet.kz/bpmn/api/v2/private/sedb2b/company/131140025304/info',
                        headers=get_response())
    return info

print(test().json())