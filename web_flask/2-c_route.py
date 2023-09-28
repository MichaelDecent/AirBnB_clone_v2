#!/usr/bin/python3
"""
this module handle a route to my home page
"""
from flask import Flask
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
    """displays C """
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=1)
