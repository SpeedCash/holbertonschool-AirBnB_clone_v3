#!/usr/bin/python3
""" This module defines the API routes to states.

Routes:
    [GET]:
        /states/: Return all States.
        /states/<state_id>: Return the State if exist or 404.

    [POST]:
        /states: Creates new state.

    [DELETE]:
        /states/<state_id>: Delete state if exist or 404.

    [PUT]:
        /states/<state_id>: Modify state if exist or 404.
"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State

@app_views.route("/states/", methods=['GET'])
def all_states():
    """ Return all instance of States. """
    all_states = storage.all(State)
    dict_states = list()
    for value in all_states.values():
        dict_states.append(value.to_dict())
    return jsonify(dict_states)


@app_views.route("/states/<state_id>", methods=['GET'])
def show_state_by_id(state_id):
    """ Return the instance of State if exist or 404. """
    state_to_show = storage.get(State, state_id)
    if state_to_show:
        return jsonify(state_to_show.to_dict())
    abort(404)


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_state_by_id(state_id):
    """ Delete instance of state if exist, else raise 404. """
    state_to_delete = storage.get(State, state_id)
    if state_to_delete:
        storage.delete(state_to_delete)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def creates_state():
    pass


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    pass
