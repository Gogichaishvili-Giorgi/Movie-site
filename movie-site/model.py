from app import db
class Movie(db.Model):
 __tablename__ = 'movies'
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String())
 year = db.Column(db.Integer())
 description = db.Column(db.String())
 typeofMovie = db.Column(db.String())

class Tvshow(db.Model):
 __tablename__ = 'tvshows'
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String())
 year = db.Column(db.Integer())
 description = db.Column(db.String())
 typeofTvshow = db.Column(db.String())

class Trailer(db.Model):
 __tablename__ = 'trailers'
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String())
 year = db.Column(db.Integer())
 description = db.Column(db.String())
 typeofTrailer = db.Column(db.String())

class Kid(db.Model):
 __tablename__ = 'kids'
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String())
 year = db.Column(db.Integer())
 description = db.Column(db.String())
 typeofKid = db.Column(db.String())
def __init__(self, name, year, description, typeofMovie):
    self.name = name
    self.year = year
    self.description = description
    self.typeofMovie = typeofMovie
def __repr__(self):
    return '<id {}>',format(self.id)

def __init__(self, name, year, description, typeofTvshow):
    self.name = name
    self.year = year
    self.description = description
    self.typeofTvshow = typeofTvshow
def __repr__(self):
    return '<id {}>',format(self.id)

def __init__(self, name, year, description, typeofTrailer):
    self.name = name
    self.year = year
    self.description = description
    self.typeofTrailer = typeofTrailer
def __repr__(self):
    return '<id {}>',format(self.id)

def __init__(self, name, year, description, typeofKid):
    self.name = name
    self.year = year
    self.description = description
    self.typeofKid = typeofKid
def __repr__(self):
    return '<id {}>',format(self.id)
def serialize(self):
    return {
        'id': self.id,
        'name': self.name,
        'year': self.year,
        'description': self.description,
        'typeofMovie': self.typeofMovie
    }

def serialize(self):
    return {
        'id': self.id,
        'name': self.name,
        'year': self.year,
        'description': self.description,
        'typeofTvshow': self.typeofTvshow
    }
def serialize(self):
    return {
        'id': self.id,
        'name': self.name,
        'year': self.year,
        'description': self.description,
        'typeofTrailer': self.typeofTrailer
    }
def serialize(self):
    return {
        'id': self.id,
        'name': self.name,
        'year': self.year,
        'description': self.description,
        'typeofKid': self.typeofKid
    }