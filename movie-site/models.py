from app import db
class Movie(db.Model):
    __tablename__= "movies"
    id = db.Column(db.Integer, primery_key=True)
    name = db.Column(db.String())
    country = db.Column(db.Integer())
    desciption = db.Column(db.String())
    typeofMovie = db.Column(db.String())


def __init__(self, name, country, desciption, typeofMovie):
    self.name = name
    self.country = country
    self.desciption = desciption
    self.typeofMovie = typeofMovie
def __repr__(self):
    return '<id {}>',format(self.id)

def serialize(self):
    return {
        'id': self.id,
        'name': self.name,
        'country': self.country,
        'description': self.desciption,
        'typeofMovie': self.typeofMovie
    }