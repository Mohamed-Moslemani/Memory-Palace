from flask import Flask
from app.config import Config
from app.extensions import mongo, jwt, bcrypt
from app.routes.auth_routes import auth_bp
from app.routes.rag_routes import rag_bp
from app.routes.password_routes import password_bp
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    mongo.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(rag_bp, url_prefix="/rag")
    app.register_blueprint(password_bp, url_prefix="/password")

    return app