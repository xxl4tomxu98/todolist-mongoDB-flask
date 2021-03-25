from flask import Flask
from .main.routes import main
from .extensions import mongo
import os

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = os.environ.get('DATABASE_URL')
    mongo.init_app(app)
    app.register_blueprint(main)
    return app