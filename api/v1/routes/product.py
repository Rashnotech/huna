#!/usr/bin/python3
"""a module that handles products """
from model import storage
from flask import request, abort, jsonify, current_app
from api.v1.routes import app_views
from model.products import Product


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def products():
    """a view function that list products"""
    
    products = storage.all(Product)
    products_list = [product.to_dict() for product in products.values()]
    if products is None:
        return jsonify({'data': []}), 200
    return jsonify({'data': products_list}), 200
