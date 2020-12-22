class Config(object):
    Debug= False
    Testing = False
    CSRF_ENABLED = True
    SEKRET_KEY = 'random_asdadad'
    SQLALCHEMY_DATABASE_URI="postgres://ryhrrstbikgwxx:7b079307f3c0ea564a38d25763c2037ed84aa6a990f2fcbc96d939eb0bf48833@ec2-34-204-22-76.compute-1.amazonaws.com:5432/d9jdlq655pat8a"

class ProductionConfig(Config):
    DEBUG = False
class Develop(Config):
    DEVELOPMENT = True
    DEBUG = False

class StegingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
class TestingConfig(Config):
    Testing = True
