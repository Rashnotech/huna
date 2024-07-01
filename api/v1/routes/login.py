#!/usr/bin/python3
"""a module for user endpoint"""
from model.user import User
from flask import request, jsonify, abort, current_app
from api.v1.routes import app_views
from flask_jwt_extended import create_access_token, jwt_required
from hashlib import md5


@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """a method that handle sign in"""
    data = request.get_json()

    if not data:
        abort(400, 'Not JSON')

    if ['email', 'password'] not in data:
        return jsonify({'error': 'Missing credentials'}), 400

    user = storage.get_email(User, data['email'])
    if user is None:
        abort(400, 'Record not found')

    if user.password != md5(data['password'].encode()):
        return jsonify({'error': 'Invalid password'})
    if user.verify is False:
        return jsonify({'error': 'Email not verified'})
    user.set_password('')
    token = create_access_token(identity=user.id)
    return jsonify({'data': user.to_dict(), 'token': token}), 200


@app_views.route('/account/<id>', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_profile(id):
    """update user profile"""
    data = request.get_json()

    if not data:
        abort(400, 'Not JSON')
    user = storage.get(User, id)
    if user is None:
        abort(400, 'Record not found')
    for attr, _ in user.items():
        for key, val in data.items():
            if attr == key:
                setattr(user, attr, val)
                user.save()
    return jsonify({'message': 'Profile updated successfully'})


@app_views.route('/account/<id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_account(id):
    """an endpoint that delete profile"""
    user = storage.get(User, id)
    if user is None:
        abort(400, 'Record not found')
    storage.delete(user)
    return jsonify({'message': 'Profile deleted successfully'})

