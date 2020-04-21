#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__, template_folder='templates')


@app.route('/states_list', strict_slashes=False)
def state_list():
    return render_template('7-states_list.html',
                           state=storage.all(State).values())


@app.teardown_appcontext
def end_session(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
