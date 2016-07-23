from mongoengine import connect

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "KSFSDFSDFSGKSDJFGKDFGJDFGJDFKASDASDASDGDFJGDFKGJDFKGJ"
    connect(
        'heroku_fj7fqx00',
        host='mongodb://resume-admin:resume-admin@ds027425.mlab.com:27425/heroku_mr51rc25',
        port=27425,
        username='resume-admin',
        password='resume-admin',
    )

#class ProductionConfig(Config):

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True