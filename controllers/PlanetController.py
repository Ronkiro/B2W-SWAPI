from flask_restful import Resource, reqparse
from models.Planet import Planet
from flask import jsonify

# SWAPI https://swapi.co/

parser = reqparse.RequestParser()
# Add current model attributes to parser
for attr in Planet.__dict__.keys():
    if attr.startswith('__'):
        continue
    parser.add_argument(attr)

class PlanetController(Resource):
    def __planets(self, id=None):
        """ Returns a py dict with planets data """
        if id:
            return Planet.objects(id=id).first()
        else:
            return Planet.objects.all()

    def __body(self):
        """ Get body args """
        args = parser.parse_args()
        return args

    # GET: /api/planeta/:?id
    def get(self, id=None):
        planet_list = self.__planets(id=id)
        if planet_list:
            return { "data": planet_list.to_json() }

    # PUT: /api/planeta/:id
    def put(self, id):
        planet = self.__planets(id=id)
        body = self.__body()
        planet.name = body['name']
        planet.climate = body['climate']
        planet.terrain = body['terrain']
        # TODO: ADD API request to update "in_movie"
        planet.save()
        
        return { "data": planet.to_json() }

    # POST: /api/planeta
    def post(self):
        pass