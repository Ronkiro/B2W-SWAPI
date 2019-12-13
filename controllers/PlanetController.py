from flask_restful import Resource, reqparse, abort
from models.Planet import Planet
import logging
from resources.SWAPI import SWAPI

# SWAPI https://swapi.co/
parser = reqparse.RequestParser()

# Add current model attributes to parser
for attr in Planet.__dict__.keys():
    if attr.startswith('__'):
        continue
    parser.add_argument(attr)

class PlanetController(Resource):
    def __planets(self, id=None, name=None):
        """ Returns a py dict with planets data """
        if name:
            return Planet.objects(name=name).first()
        elif id:
            return Planet.objects(id=id).first()
        else:
            return Planet.objects.all()

    def __body(self):
        """ Get body args """
        args = parser.parse_args()
        return args

    # GET: /api/planeta/:?id
    def get(self, id=None, name=None):
        planet_list = self.__planets(id=id, name=name)
        if planet_list:
            return { "data": planet_list.to_json() }
        else:
            return { "data": {} }

    # DELETE: /api/planets
    def delete(self, id=None, name=None):
        if any([name, id]):
            planet = self.__planets(id=id, name=name)
            if planet:
                planet.delete()
                planet.save()
                return 204
            return abort(404)
        return abort(400)

    # POST: /api/planet
    def post(self):
        planet_count = Planet.objects.count()
        planet = Planet(id=planet_count)
        body = self.__body()
        planet.name = body['name']
        planet.climate = body['climate']
        planet.terrain = body['terrain']
        planet.in_movie = SWAPI().get_movie_count(body['name'])
        planet.save()
        
        return { "data": planet.to_json() }, 201