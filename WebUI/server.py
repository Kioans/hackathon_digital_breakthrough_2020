from flask import Flask, Response, request
import datetime

app = Flask(__name__)
db = [
    {'text': 'Не работает Интернет',
     'User': 'User1',
     'time': datetime.datetime.now()
     },
]

@app.route("/")
def hello():
    return "Hello world"

@app.route("/send",methods=['POST'])
def send_message():
    data = request.json
    text = data['text']
    author = data['author']
    db.append({
        'text': text,
        'User': author,
        'time': datetime.datetime.now()
    })
    print(author, text)
    return Response("ok")

@app.route("/recive",methods=['POST'])
def send_message():
    data = request.json
    text = data['text']
    author = data['author']
    db.append({
        'text': text,
        'User': author,
        'time': datetime.datetime.now()
    })
    print(author, text)
    return Response("ok")


@app.route("/get")
def get_messages():
    return {'data': db}


app.run()
