from flask import Flask
from flask_mongoengine import MongoEngine
import os 

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT,'static/')

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = MongoEngine(app)

app._static_folder = STATIC_ROOT

app.debug =True

def register_blueprints(app) :
    from resume.views import index
    app.register_blueprint(index)
register_blueprints(app)

if __name__ == '__main__' :
    app.run()
