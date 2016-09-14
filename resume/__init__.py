from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_bcrypt import Bcrypt
import os 

#init
app = Flask(__name__)

#Global Variables
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT,'_static/')

#static
app._static_folder = STATIC_ROOT

#config
CONFIG_TYPE = os.environ.get('CONFIG_TYPE','DevelopmentConfig');
app.config.from_object('config.'+ CONFIG_TYPE)
app.debug = app.config.get('DEBUG')

#database
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

#bcrypt
flask_bcrypt = Bcrypt(app)

def register_blueprints(app) :
    from resume.views import index
    from tumblelog.views import tumblelog
    from user.views import user
    app.register_blueprint(index)
    app.register_blueprint(tumblelog)
    app.register_blueprint(user)
register_blueprints(app)

if __name__ == '__main__' :
    app.run()
