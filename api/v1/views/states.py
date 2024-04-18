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
    """ Create instance of state. """
    # Get JSON data of the body request sent by POST.
    req_json = request.get_json()
    # Check if Data is not none and had name.
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if "name" not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)
    new_state = State()
    # Loops to set each key:value to the new state.
    for (key, value) in req_json.items():
        setattr(new_state, key, value)
    # Save Data.
    storage.new(new_state)
    storage.save()
    return make_response(jsonify(new_state.to_dict()), 201)
    


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Modify instance of state if exist, else raise 404. """
    target_state = storage.get(State, state_id)
    # Check if object exist.
    if target_state is None:
        return make_response(jsonify({"error": "Not found"}), 404)
    body_json = request.get_json()
    if body_json is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    # Loops to update each key:value to the state.
    for (key, value) in body_json.items():
        setattr(target_state, key, value)
    # Save Data
    target_state.save()
    return make_response(jsonify(target_state.to_dict()), 200)
    