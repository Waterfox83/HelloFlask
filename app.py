from flask import Flask
import os
app = Flask(__name__)


@app.route("/")
def hello():
    hero_name = os.environ.get('hero_name', 'Maeve')
    superhero_name = os.environ.get('superhero_name', 'Homelander')
    welcome_string = "Hello "+hero_name+" and " + superhero_name
    print(welcome_string)
    return "<html><body><h2>"+ welcome_string + "</h2></body></html>\n"


@app.route('/hello')
def say_hello():
    return 'Say hello!'


if __name__ == '__main__':
    app.run()
