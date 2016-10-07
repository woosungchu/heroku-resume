from flask.views import MethodView
from flask import Blueprint, render_template

index = Blueprint('index',__name__,template_folder='_templates')

class Index(MethodView):
    
    stacks = {
        #'Favorite Dev-Env':'Python, Flask, Backbone, MongoDB',
        #'Skills':'Java, Spring, Python, Django, Flask, Backbone, Ember, Bootstrap, Mssql, Mysql, Oracle, MongoDB',
        
        'Language':'Java, Python',
        'Framework':'Spring, Django, Flask, Ember, Bootstrap',
        'OS':'Window, Ubuntu',
        'sql':'Mssql, Mysql, Oracle, MongoDB',
    }
    
    def get_context(self):
        welcome = 'Hello HeroKu'
        
        context = {
            'welcome':welcome,
            'stacks':self.stacks
        }
        return context
        
    def get(self):
        context = self.get_context()
        return render_template('list.html', **context)


index.add_url_rule('/',view_func= Index.as_view('index'))

