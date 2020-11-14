import requests

while True:
    answ= input()
    response = requests.post(
        'http://localhost:5000/',
        json={'text': answ, 'author': 'Bot'}
    )

