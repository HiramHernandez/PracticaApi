import os
from datetime import timedelta

from dotenv import load_dotenv
# BITSON imports

# Ruta base del proyecto
BASEDIR = os.path.dirname(os.path.abspath(__file__))

#ruta del archivo de variables de entorno ".env"
ENV_VARS = os.path.join(BASEDIR, ".env")
#Se cargan las varibles de entorno
load_dotenv(ENV_VARS)

class Config:
    """Base config class"""
    PROJECT_NAME = os.environ.get('PROJECT_NAME')
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_SERVICE = os.environ.get('DB_SERVICE')
    DB_NAME = os.environ.get('DB_NAME')

    LOG_IN_DB = {
        'OPTIONS': [],
        'GET': [],
        'POST': [201, 200, 400],
        'PUT': [200, 401],
        'DELETE': [204, 400]
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SLOW_QUERY_TIMEOUT = 0.5
    SQLALCHEMY_RECORD_QUERIES = False

    WTF_CSRF_ENABLED = False

    @staticmethod
    def init_app(app):
        pass
