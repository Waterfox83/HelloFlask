from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "<html><body><h1>Hello Best Bike App!</h1></body></html>\n"


@app.route('/hello')
def say_hello():
    return 'Say hello!'


if __name__ == '__main__':
    app.run()
