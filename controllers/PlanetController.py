from flask_restful import Resource
from models.Planet import Planet
from flask import jsonify

class PlanetController(Resource):
    def __planets(self, id=None):
        """ Returns a py dict with planets data """
        if id:
            return Planet.objects(id=id).first()
        else:
            return Planet.objects.all()

    # GET: /api/planeta/:?id
    def get(self, id=None):
        planet_list = self.__planets(id=id)
        if planet_list:
            return { "data": planet_list.to_json() }

    # PUT: /api/planeta
    def put(self):
        pass

    # POST: /api/planeta
    def post(self):
        pass