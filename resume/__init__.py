from flask import Flask , Blueprint

app = Flask(__name__)

def register_blueprints(app) :
    from resume.views import index
    app.register_blueprint(index)
register_blueprints(app)

if __name__ == '__main__' :
    app.run(DEBUG=True)
