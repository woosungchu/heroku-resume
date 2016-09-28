from flask.views import MethodView
from flask import Blueprint, render_template

index = Blueprint('index',__name__,template_folder='_templates')

class Index(MethodView):
    
    stacks = {
        'Language':'Java, Python',
        'Framework':'Spring, Django, Flask, Ember, Bootstrap',
#        'SQL':'Mssql,Mysql,Oracle,MongoDB',
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

