#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Returns a string with 'C' followed by the provided text.
    Replaces underscores with spaces in the text.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route(
    '/python/',
    defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Returns a string with 'Python' followed by the provided text.
    Replaces underscores with spaces in the text.
    If no text is provided, uses 'is cool' as the default text.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Returns a string stating that the provided number is a number.
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
