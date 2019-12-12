from flask import Flask
from routes import setup_routes
from mongoengine import connect
import logging
from dotenv import load_dotenv, find_dotenv
from os import getenv

logging.basicConfig()

logging.info(f"Starting app...")
app = Flask(__name__)
logging.info(f"Trying to read .env")
load_dotenv(find_dotenv())
logging.info(f"Trying to read app.cfg")
app.config.from_pyfile('app.cfg')

logging.info(f"Trying to connect to {app.config['DATABASE_HOST']}...")
connect (
        getenv('DATABASE_NAME', app.config['DATABASE_NAME']), 
        alias='planet-db-alias',
        host=getenv('DATABASE_HOST', app.config['DATABASE_HOST']),
        port=getenv('DATABASE_PORT', app.config['DATABASE_PORT']),
        username=getenv('DATABASE_USER', app.config['DATABASE_USER']),
        password=getenv('DATABASE_PASSWORD', app.config['DATABASE_PASSWORD']),
        authentication_source='admin'
)
setup_routes(app)


if __name__ == '__main__':
    debug_mode = True if getenv('DEBUG', app.config['DEBUG']).lower() == 'true' else False
    app.run(debug=debug_mode)