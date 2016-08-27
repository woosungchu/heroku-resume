from mongoengine import connect
import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #DB
    MONGODB_SETTINGS = {
        'db':'dev',
        'host': os.environ.get('DB_DEV_URI')
    }

class ProductionConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db':'production',
        'host': os.environ.get('DB_PRO_URI')
    }

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    