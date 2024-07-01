#!/usr/bin/python3
"""config file"""
import os
from datetime import timedelta


class Config:
    """ a class for config """
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'downloaded')
    SECRET_KEY = "think about it"
    JWT_SECRET_KEY = "think about it"
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=2)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    @classmethod
    def init_app(cls, app):
        pass
