#!/usr/bin/python3
"""a module that handle registration"""
from api.v1.routes import app_views
from flask import jsonify, request, abort, current_app
from models import storage
from os import getenv
import asyncio
from flask_mail import Message, Mail
from models.user import User


@app_views.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    """an endpoint that handles registration"""
    data = request.get_json()

    if not data:
        abort(400, 'Not JSON')

    for attr, _ in data.keys():
        if attr not in ['username', 'firstname', 'lastname', 'email', 'password']:
            return jsonify({'error': f'Missing {attr}'})
    email = data.get('email')
    user = storage.get_email(email)
    if user and user.verify == True:
        return jsonify({'error': 'Email already exist'})
    if user and user.verify == False:
        response, status = send_mail(email)
        if status == 500:
            return 
        return jsonify({'message': 'Verification email sent'})
    response, status = asyncio.run(send_mail(email, body))
    if status == 500:
        abort(400, response)
    new_user = User(**data)
    new_user.save()
    new_user.set_password('')
    return jsonify({'message': 'Account created',
                    'data': new_user.to_dict()}), 201


    async def send_mail(receiver, body):
        """a function that send verification mail"""
        mail = Mail(current_app)
        with mail.connect() as conn:
            msg = Message(
                    subject='HUNA Store Verification',
                    sender=getenv('EMAIL'),
                    recipients=[receiver],
                    html=body)
            try:
                mail.send(msg)
                return jsonify({'message': 'Email sent successfully'})
            except Exception as e:
                return jsonify({'message': f'Error sending email: {str(e)}'}), 500
