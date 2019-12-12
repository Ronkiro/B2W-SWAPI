from flask_restful import Resource, reqparse
from models.Planet import Planet
from flask import jsonify
import logging
import json
import requests

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

    def __request_planets(self, page):
        r = requests.get(f'https://swapi.co/api/planets?page={page}')
        return json.loads(r.content)

    def __SWAPI_planets(self):
        result_list = []
        page = 1
        content = self.__request_planets(page)
        while(1):
            print(content['next'])
            result_list += content['results']
            if content['next'] is None:             # if no next page
                break                               # stop parsing
            page += 1                               # else keep
            content = self.__request_planets(page)
        return result_list

    # GET: /api/planeta/:?id
    def get(self, id=None):
        planet_list = self.__planets(id=id)
        if planet_list:
            return { "data": planet_list.to_json() }
        else:
            return { "data": {} }

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

    # DELETE: /api/planets
    def delete(self, id):
        planet = self.__planets(id=id)
        if planet:
            planet.delete()
            planet.save()
            return 204

    # POST: /api/planet
    def post(self):
        planet_count = Planet.objects.count()
        planet = Planet(id=planet_count)
        body = self.__body()
        planet.name = body['name']
        planet.climate = body['climate']
        planet.terrain = body['terrain']
        # TODO: ADD API request to update "in_movie"
        planet.save()
        
        return { "data": planet.to_json() }, 201