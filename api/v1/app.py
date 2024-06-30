#!/usr/bin/env python3
"""app entry point"""
from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from model import storage
from api.v1.config import Config
from api.v1.routes import app_views
from flask_jwt_extended import JWTManager


app = Flask(__name__)

config_name = 'development'
app.config.from_object(Config)
mail = Mail()
mail.init_app(app)
CORS(app, resources={},)
app.register_blueprint(app_views)
jwt = JWTManager(app)


@app.teardown_appcontext
def teardown_appcontext(self):
    """Teardown app context"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """Not found error"""
    return jsonify({'error': "Not found"})

@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden error"""
    return jsonify({'error': 'Forbidden'})

if __name__ == '__main__':
    app.run(debug=True)
