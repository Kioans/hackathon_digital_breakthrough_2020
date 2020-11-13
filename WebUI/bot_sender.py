import requests

while True:
    answ= input()
    response = requests.post(
        'http://localhost:5000/send',
        json={'text': answ, 'author': 'Bot'}
    )
