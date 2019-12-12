from flask_restful import Api
from controllers.PlanetController import PlanetController

def setup_routes(app):
    api = Api(app)
    api.add_resource(PlanetController, '/api/planets')