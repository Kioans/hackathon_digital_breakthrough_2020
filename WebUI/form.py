from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


@app.route("/recive", methods=['POST'])
def handle_event():
    data = request.json
    print('received event: ' + str(data))
    socketio.emit('response', data, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
