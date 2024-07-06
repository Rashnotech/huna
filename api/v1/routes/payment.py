#!/usr/bin/python3
"""a module that handle payment"""
from api.v1.routes import app_views
from models import storage
from flask import request, jsonify, abort
from models.payment import Payment
from models.order import Order


@app_views.route('/payments/<id>', methods=['POST'], strict_slashes=False)
def payment(id):
    """a function that handles payment"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    amount = data.get('amount')
    method = data.get('payment_method', 'default')
    if not amount:
        return jsonify({'error': 'Amount is required'}), 400

    if method not in ['default', 'installment']:
        return jsonify({'error': 'Invalid payment method'}), 400
    try:
        order = storage.get(Order, id)
    except Exception:
        return jsonify({'error': 'Order not found'}), 404

    try:
        new_payment = Payment()
        if method == 'installment':
            new_payment.calculate_installment()
        new_order.save()
        return jsonify(new_payment.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except IntegrityError:
        storage.rollback()
        return jsonify({'error': 'Payment could not be processed'})
    except Exception as e:
        storage.rollback()
        return jsonify({'error': str(e)}), 500

