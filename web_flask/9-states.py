#!/usr/bin/python3
'''a script that starts a Flask web application'''

from models import storage
from models.state import State
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    '''Tear down seesion: db'''
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    '''Print for each state: id & name'''
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    '''Return states and cities if id is instates'''
    states = storage.all(State)
    key = 'State.{}'.format(id)
    state = states.get(key)
    return render_template('9-states.html', state=state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
