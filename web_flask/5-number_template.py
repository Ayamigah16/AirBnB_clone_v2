#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)

hhhh
@app.route('/', strict_slashes=False)
def hello():
    """
    Returns a greeting message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Returns a string with 'C' followed by the provided text.
    Underscores in the text are replaced with spaces.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route(
    '/python/',
    defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Returns a string with 'Python' followed by the provided text.
    Underscores in the text are replaced with spaces.
    If no text is provided, the default text 'is cool' is used.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Returns a string indicating that the provided number is a number.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders an HTML template with the provided number.
    The number is passed to the template as a variable 'n'.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
