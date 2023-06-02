from threading import Thread

from flask import Flask, request, jsonify

from ActiveMQ.AMQListener import AMQListener

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/hello', methods=['POST'])
def hello():
    data = {'name': 'python'}
    return jsonify(data)


def flask_thread():
    app.run()


def schedule_task():
    aMQListener = AMQListener()
    aMQListener.loop_monitor()


if __name__ == '__main__':
    scheduler_thread = Thread(target=schedule_task)
    scheduler_thread.start()
    flask_thread = Thread(target=flask_thread)
    flask_thread.start()
