from flask_restful import Resource

class PlanetaController(Resource):

    # GET: /api/planeta
    def get(self):
        return {'hello': 'world'}
    
    # PUT: /api/planeta
    def put(self):
        pass

    # POST: /api/planeta
    def post(self):
        pass