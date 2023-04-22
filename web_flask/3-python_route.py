#!/usr/bin/python3
'''a script that starts a Flask web application'''

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_HBNH():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    text = escape(text)
    string = text.replace('_', ' ')
    return 'C {}'.format(string)


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
