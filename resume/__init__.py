from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = MongoEngine(app)

app = Flask(__name__)

def register_blueprints(app) :
    from resume.views import index
    app.register_blueprint(index)
register_blueprints(app)

if __name__ == '__main__' :
    app.run()
