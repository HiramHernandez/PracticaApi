from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

api = Api(version='v0.1', title='Tutorial API', description='tutorial para aprender a crear un API RESTful en Python')
db = SQLAlchemy()

migrate = Migrate()

