#!/usr/bin/python3
"""a module that handles products """
from model import storage
from flask import abort, jsonify, current_app
from api.v1.routes import app_views
from model.products import Product
from model.specs import Specification
from model.desc import Description


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def products():
    """a view function that list products"""
    
    products = storage.all(Product)
    products_list = [product.to_dict() for product in products.values()]
    if products is None:
        return jsonify({'data': []}), 200
    return jsonify({'data': products_list}), 200


@app_views.route('/product/<id>', methods=['GET'], strict_slashes=False)
def find_products(id):
    product = storage.get(Product, id)
    if product is None:
        return jsonify({'data': []}), 200
    return jsonify({'data': product.to_dict()}), 200

@app_views.route('/product/image/<name>', methods=['GET'], strict_slashes=False)
def product_image(name):
    from flask import send_from_directory
    """fetch product image"""
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], name)
