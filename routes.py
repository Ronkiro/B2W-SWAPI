from flask_restful import Api
from controllers.HelloWorld import HelloWorld
from controllers.PlanetaController import PlanetaController

def setup_routes(app):
    api = Api(app)
    api.add_resource(HelloWorld, '/api/hello')
    api.add_resource(PlanetaController, '/api/planeta')