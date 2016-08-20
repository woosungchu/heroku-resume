from flask import Flask
from flask_mongoengine import MongoEngine
import os 

#Global Variables
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT,'_static/')

#init
app = Flask(__name__)

#config
app.config.from_object('config.DevelopmentConfig')

#database
db = MongoEngine(app)
#static
app._static_folder = STATIC_ROOT

app.debug =True

def register_blueprints(app) :
    from resume.views import index
    from tumblelog.views import tumblelog
    app.register_blueprint(index)
    app.register_blueprint(tumblelog)
register_blueprints(app)

if __name__ == '__main__' :
    app.run()
