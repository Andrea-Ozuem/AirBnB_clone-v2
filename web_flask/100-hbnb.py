#!/usr/bin/python3
'''a script that starts a Flask web application has routes for
hbnb airBnB clone
'''

from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    '''Tear down seesion: db'''
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Print for each state: id & name'''
    states = list(storage.all(State).values())
    places = list(storage.all(Place).values())
    amenities = list(storage.all(Amenity).values())
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
