import base64
import uuid
import requests

def send_code(to_number: str, text: str):

    url = 'http://{URL}'
    username = '{USERNAME}'
    password = '{PASSWORD}'

    blended_string = username + ":" + password

    message_bytes = blended_string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes).decode('ascii')

    token = 'Basic ' + base64_bytes

    headers = {
        'Content-type': 'application/json',  # Определение типа данных
        'Accept': 'text/plain',
        'Authorization': token
    }

    data = {
        "messages":
            [
                {
                    "recipient": "998"+to_number,
                    "message-id": str(uuid.uuid4()),

                    "sms": {

                        "originator": "3700",
                        "content": {
                            "text": text
                        }
                    }
                }
            ]
    }  # Если по одному ключу находится несколько словарей, формируем список словарей
    response = requests.post(url, json=data, headers=headers)
    print(response.text)


def send_sms(to_number: str, text: str, current_user, db):
    url = 'http://{URL}'
    username = '{USERNAME}'
    password = '{PASSWORD}'

    blended_string = username + ":" + password

    message_bytes = blended_string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes).decode('ascii')

    token = 'Basic ' + base64_bytes

    headers = {
        'Content-type': 'application/json',  # Определение типа данных
        'Accept': 'text/plain',
        'Authorization': token
    }

    data = {
        "messages":
            [
                {
                    "recipient": to_number,
                    "message-id": str(uuid.uuid4()),

                    "sms": {

                        "originator": "3700",
                        "content": {
                            "text": text
                        }
                    }
                }
            ]
    }  # Если по одному ключу находится несколько словарей, формируем список словарей
    response = requests.post(url, json=data, headers=headers)

    print(response.text)

    return response.text

# print("Telefon raqamini kiriting:")
# x = input()

# print("Xabarni kiriting:")
# y = input()

# send_code(to_number=str(x), text=str(y))
