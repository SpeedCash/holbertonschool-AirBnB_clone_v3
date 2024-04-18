#!/usr/bin/python3
""" This module defines the API routes to states.

Routes:
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/states/", methods=['GET'])
def states():
    """ Return a dict of all States """
    all_states = storage.all("State")
    dict_states = list()
    for value in all_states.values():
        dict_states.append(value.to_dict())
    return jsonify(dict_states)
