from flask import Flask
from flask_mongoengine import MongoEngine
import os 

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = MongoEngine(app)

app._static_folder = os.path.abspath("static")

app.debug =True

def register_blueprints(app) :
    from resume.views import index
    app.register_blueprint(index)
register_blueprints(app)

if __name__ == '__main__' :
    app.run()
