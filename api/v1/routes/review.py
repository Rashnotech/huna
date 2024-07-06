#!/usr/bin/python3
"""a module that handle customer review"""
from models import storage
from models.reviews import Review
from flask import jsonify, request, abort
from api.v1.routes import app_views
from models.user import User
from models.products import Product


@app_views.route('/review', methods=['POST'], strict_slashes=False)
def review():
    """a function that review products"""
    data = request.get_json()

    if not data:
        abort(400, 'Not JSON')
    user_id, product_id, _ = data
    for attr in ['comment', 'product_id', 'user_id', 'rating']:
        if attr not in data.keys():
            return jsonify({'error': f'Missing {attr}'})
    user = storage.get(User, user_id)
    if not user:
        abort(400, 'User not found')
    product = storage.get(Product, product_id)
    if not product:
        abort(400, 'Product not found')
    new_review = Review(**data)
    new_review.save()
    return jsonify({'message': 'Review added successfully'}), 200


@app_views.route('/review/<product_id>', methods=['GET'], strict_slashes=False)
def fetch_review(product_id):
    """a function that fetch review of a product"""
    reviews = storage.get_product(Review, product_id)
    return jsonify({'data': reviews.to_dict()}), 200


@app_views.route('/review/<id>', methods=['GET'], strict_slashes=False)
def delete_review(id):
    """a function that delete a review"""
    review = storage.get(Review, id)
    storage.delete(review)
    return jsonify({'message': 'Review deleted'}), 200


@app_views.routes('/review/<id>', methods=['PUT'], strict_slashes=False)
def updated_review(id):
    """a function that update review"""
    review = storage.get(Review, id)
    if not review:
        abort(400, 'Not JSON')
    for attr, _ in review.items():
        for key, val in data.items():
            if attr == key:
                setattr(review, attr, val)
                review.save()
    return jsonify({'message': 'Review updated successfully'}), 200
