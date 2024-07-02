#!/usr/bin/python3
"""a module that handle orders"""
from model import storage
from model.order import Order, Item
from flask import jsonify, abort, request
from api.v1.routes import app_views
from model.user import User


@app_views.route('/cart', methods=['POST'], strict_slashes=False)
def order_items():
    """a function that handles ordered items"""
    data = request.get_json()
    if not data:
        abort(400, 'Not JSON')
    for dt in data:
        product = storage.get(Product, dt.product_id)
        if not product:
            return jsonify({'error': 'Product not found'})
        new_item = Item(**dt)
        new_item.save()
    return jsonify({data})


@app_views.route('/', methods=['POST'], strict_slashes=False)
def order():
    pass
