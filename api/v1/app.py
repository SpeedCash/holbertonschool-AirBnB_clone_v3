#!/usr/bin/python3
""" This module defines an API. """
from api.v1.views import app_views
from flask import Flask
import os
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(self):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', default="0.0.0.0")
    port = os.getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=port, threaded=True)
