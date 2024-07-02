#!/usr/bin/python3
"""a module that handle payment"""
from api.v1.routes import app_views
from model import storage
from flask import jsonify, abort
from model.payment import Payment
from model.orders import Order


@app_views.route('/payments/<id>', methods=['POST'], strict_slashes=False)
def payment(id):
    """a function that handles payment"""
    data = request.get_json()
    order = storage.get(Order, id)
    amount, _ = data
    if amount == :
    new_order = Order(**data)
    new_order.save()
    return jsonify({}), 200
