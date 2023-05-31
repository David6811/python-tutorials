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


if __name__ == '__main__':
    aMQListener = AMQListener()
    aMQListener.loop_monitor()
    app.run()
