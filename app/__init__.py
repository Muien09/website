from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '59c7a3a05300b593e0d9fba858063a54'  # Updated secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    #app.config['SENDGRID_API_KEY'] = os.getenv('SENDGRID_API_KEY')

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
