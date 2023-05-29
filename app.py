from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/hello', methods=['POST'])
def hello():
    data = {'name': 'python'}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
