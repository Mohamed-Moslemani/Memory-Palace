from flask import Flask
from flask_cors import CORS
from app.extensions import mongo, bcrypt, jwt
from app.routes import auth




def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    mongo.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)
    app.register_blueprint(auth, url_prefix="/api",name='authroute')

    return app
