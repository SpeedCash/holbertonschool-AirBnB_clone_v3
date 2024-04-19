#!/usr/bin/python3
""" This Module defines the Blueprint app_views"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# The nexts lines raise an error pycodestyle, it's normal.
from api.v1.views.index import *
from api.v1.views import states, cities, amenities, users, places, places_reviews
