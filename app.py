import os

from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from app.model.hotel import Hotel
from app.backend import create_api

#Creación del API con un método externo extraido del archivo backend
app = create_api(os.getenv('FLASK_CONFIG') or 'default')

#La aplicación esta ejecuntadose, se inlcuye algun comando util
if __name__ == '__main__':
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.add_command("runserver", Server(threaded=False, port=9001))
    manager.run(default_command='runserver')
