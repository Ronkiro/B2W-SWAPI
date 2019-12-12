import mongoengine

class Planet(mongoengine.Document):
    exclude = ['id', 'in_movie'] # Delete the need from body requests
    id = mongoengine.IntField(primary_key=True)
    name = mongoengine.StringField(max_length=50, required=True)
    climate = mongoengine.StringField(max_length=50, required=True)
    terrain = mongoengine.StringField(max_length=50, required=True)
    in_movie = mongoengine.IntField(default=0)