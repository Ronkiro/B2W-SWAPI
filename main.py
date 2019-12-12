from flask import Flask
from routes import setup_routes
from mongoengine import connect
import logging

logging.basicConfig()

logging.info(f"Starting app...")
app = Flask(__name__)
logging.info(f"Trying to read app.cfg")
app.config.from_pyfile('app.cfg')

logging.info(f"Trying to connect to {app.config['DATABASE_HOST']}...")
connect (
        app.config['DATABASE_NAME'], 
        alias='planet-db-alias',
        host=app.config['DATABASE_HOST'],
        port=app.config['DATABASE_PORT'],
        username=app.config['DATABASE_USER'],
        password=app.config['DATABASE_PASSWORD'],
        authentication_source='admin'
)
setup_routes(app)


if __name__ == '__main__':
    debug_mode = True if app.config['DEBUG'].lower() == 'true' else False
    app.run(debug=False)