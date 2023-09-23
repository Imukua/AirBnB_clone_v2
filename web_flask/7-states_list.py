#!/usr/bin/python3
"""Starts a Flask web app
listens on 0.0.0.0, port 5000
routes:
    /states_list: HTML page with a list of all State objects in DBStorage
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """displays an HTML page with a list of all State objects in DBStorage

    states are sorted by name
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """clear the current  session of SQLAlchemy"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
