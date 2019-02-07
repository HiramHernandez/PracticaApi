from flask import Flask
from flask_cors import CORS
from app.extensions import api, db, migrate
from app.api.hotel_api import hotels
from config import Config

NAMESPACES = [
    hotels
]

def create_api(environment_name=None):
    for namespace in NAMESPACES:
        api.add_namespace(namespace)
    app = Flask(__name__)
    #app.config.from_object(config[environment_name])
    app.config.from_object(Config)
    CORS(app)
    with app.app_context():
        
        db.init_app(app)
        db.create_all()
        migrate.init_app(app, db)
        api.init_app(app)
    return app
