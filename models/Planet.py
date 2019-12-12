import mongoengine

class Planeta(mongoengine.Document):
    id = mongoengine.IntField(primary_key=True)
    name = mongoengine.StringField(max_length=50, required=True)
    climate = mongoengine.StringField(max_length=50, required=True)
    terrain = mongoengine.StringField(max_length=50, required=True)
    in_movie = mongoengine.IntField(default=0)