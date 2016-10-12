from mongoengine import connect
import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_HOST = os.environ.get('DB_DEV_URI')
    #DB
    MONGODB_SETTINGS = {
        'db':'dev',
        'host': DB_HOST
    }

class ProductionConfig(Config):
    DEBUG = False
    DB_HOST = os.environ.get('DB_PRO_URI')
    MONGODB_SETTINGS = {
        'db':'production',
        'host': DB_HOST
    }

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    