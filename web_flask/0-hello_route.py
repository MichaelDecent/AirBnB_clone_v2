#!/usr/bin/python3
"""
this module handle a route to my home page
"""
from web_flask import app


@app.route('/', strict_slashes=False)
def hello_page():
    """ This returns a string """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
