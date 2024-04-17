#!/usr/bin/python3
""" This module defines the routes for API.

Routes:
    /status: display JSON status --> 'OK'.
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """return JSON status: OK."""
    return jsonify({'status': 'OK'})
