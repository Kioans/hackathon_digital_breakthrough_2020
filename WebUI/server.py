from flask import Flask, Response, request, render_template
import datetime

app = Flask(__name__)
db = [
    {'text': 'Не работает Интернет',
     'User': 'User1',
     'time': datetime.datetime.now()
     },
]
authors = ['asd','aqwe']

@app.route("/", methods=['GET', 'POST'])
def send_message():
    data = request.json
    print(db)
    text = db[0]['text']
    if data is not None:
        text = data['text']
        author = data['author']
        db.insert(0, {
            'text': text,
            'User': author,
            'time': datetime.datetime.now()
        })
        print(author, text)

    return render_template("chat.html", database=authors)


@app.route("/recive", methods=['GET'])
def res_message():
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
