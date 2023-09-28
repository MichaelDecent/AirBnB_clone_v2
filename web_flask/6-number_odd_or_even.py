#!/usr/bin/python3
"""
this module handle a route to my home page
"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_page():
    """ This returns a string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB_page():
    """ Returns 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """displays C with additional text"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text=None):
    """displays python with additional text"""
    if text is None:
        text = 'is cool'

    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>')
def number_n(n):
    """displays a n if it is an integer"""
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """ display a template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ returns n if odd or even """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=1)
