#!/usr/bin/python3
"""
This Module handles a route that returns a list of states
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """This displays return an html of a list of states """
    states = [st for st in storage.all(State).values()]
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(self):
    """Ends the database session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=1)
