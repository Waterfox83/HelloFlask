from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def say_hello():
    return 'Say hello!'


if __name__ == '__main__':
    app.run()
