#!/usr/bin/env python3
"""A model containing the main app"""

from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_note_found(error):
    """Handles the 404 error """
    return make_response(jsonify({"error":"Not found"}), 404)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True)