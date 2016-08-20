from flask.views import MethodView
from flask import Blueprint, render_template

index = Blueprint('index',__name__,template_folder='_templates')

class Index(MethodView):
    def get(self):
        welcome = 'Hello HeroKu'
        return render_template('list.html', welcome = welcome)


index.add_url_rule('/',view_func= Index.as_view('index'))

