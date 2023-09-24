from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list')
def state_list():
    """This displays return an html of a list of states """
    states = storage.all(State)
    return render_template('7-states_list.html', states)


@app.teardown_appcontext
def remove_current_session():
    """ remove the current SQLAlchemy Session """
    storage.close()
