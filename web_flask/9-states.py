#!/usr/bin/python3
"""
this handles a route for states with ids
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def state_list():
    """This displays return an html of a list of states """
    states = [st for st in storage.all(State).values()]
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=True)
def display_states(id=None):
    """this return an html file for the cities of state"""
    states = [st for st in storage.all(State).values()]
    state_obj = None
    for state in states:
        if state.id == id:
            state_obj = state
    return render_template('9-states.html', state_obj=state_obj)


@app.teardown_appcontext
def teardown(self):
    """Closes Database Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
