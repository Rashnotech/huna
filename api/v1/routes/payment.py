#!/usr/bin/python3
"""a module that handle payment"""
from api.v1.routes import app_views
from model import storage
from flask import jsonify, abort
from model.payment import Payment


@app_views.route('/payments/<>', methods=['GET'], strict_slashes=False)
def payment():
    """a function that handles payment"""
    return jsonify({}), 200
