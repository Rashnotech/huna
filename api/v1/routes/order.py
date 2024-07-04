#!/usr/bin/python3
"""a module that handle orders"""
from model import storage
from model.order import Order, Item
from flask import jsonify, abort, request
from api.v1.routes import app_views
from model.user import User
from os import getenv
import requests


@app_views.route('/cart', methods=['POST'], strict_slashes=False)
def order_items():
    """a function that handles ordered items"""
    data = request.get_json()
    if not data:
        abort(400, 'Not JSON')
    user_id = data.get('user_id')
    product = storage.get(Product, dt.product_id)
    if not product:
        return jsonify({'error': 'Product not found'})
    new_item = Item(**dt)
    new_item.save()
    status = 'default'
    payload = {'user_id': user_id, 'status': 'pending',
                'order_item': new_item.id}
    status, message = requests.post('{}/{}'.format(getenv('BASEURL'),
                                    '/api/v1/orders'), payload)
    return jsonify({'message': 'Item orders successfully'}), 200


@app_views.route('/orders/', methods=['POST'], strict_slashes=False)
def order():
    """a function that handles order"""
    data = request.get_json()
    if not data:
        abort(400, 'Not JSON')
    user_id = data.get('user_id')
    order_id = data.get('order_id')
    user = storage.get(User, user_id)
    if not user:
        return jsonify({'error': 'No user found'}), 400
    order = storage.get(Item, order_id)
    if not order:
        return jsonify({'error': 'No order found'}), 400
    new_order = Order(**data)
    new_order.save()
    return jsonify({'message': 'order added'}), 200


@app_views.route('', methods=['PUT'], strict_slashes=False)
def update_order():
    """a function that updates orders"""
    pass
