#!/usr/bin/python3
"""Blueprint for the api"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1', template_folder='templates')


from api.v1.routes.signup import *
from api.v1.routes.login import *
from api.v1.routes.product import *
