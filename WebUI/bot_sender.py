import requests

x = 3
while True:
    answ= input()
    x += 1
    response = requests.post(
        f'http://localhost:5000/ai-quotes/',
        json= {
            "id": x,
            "author": "Bot",
            "quote": answ
        }
        )
    print(response.text)
