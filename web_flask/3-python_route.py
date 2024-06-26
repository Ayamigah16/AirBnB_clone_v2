#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.
    Returns: 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the '/hbnb' URL.
    Returns: 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Route handler for the '/c/<text>' URL.
    Replaces underscores in the text with spaces.
    Args:
        text (str): The text to be displayed after 'C'.
    Returns: 'C <text>'
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route(
    '/python/',
    defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Route handler for the '/python/' and '/python/<text>' URLs.
    Replaces underscores in the text with spaces.
    Args:
        text (str): The text to be displayed after 'Python'.
    Returns: 'Python <text>'
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
