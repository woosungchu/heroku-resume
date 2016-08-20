from flask import Blueprint, render_template, request , redirect , url_for
from flask.views import MethodView
from tumblelog.models import Post
from flask_mongoengine.wtf import model_form


ROOT = '/tumblelog/'
tumblelog = Blueprint('tumblelog',__name__,template_folder='_templates'+ROOT)

class ListView(MethodView):
    
    form = model_form(Post, exclude=['created_at'])
    
    def get_context(self):
        posts = Post.objects.all()
        form = self.form(request.form)
        welcome = 'Hello Tumblelog'
        
        context = {
            "posts" : posts,
            "form" : form,
            "welcome" : welcome 
        }
        return context
    
    def get(self):
        context = self.get_context()
        return render_template(ROOT+'list.html', **context)
    
    def post(self):
        context = self.get_context()
        form = context.get('form')
        
        if form.validate():
            post = Post()
            form.populate_obj(post)
            post.save()
            
            return redirect(url_for('tumblelog.list'))
        return render_template(ROOT+'list.html', **context)
        


tumblelog.add_url_rule(ROOT,view_func= ListView.as_view('list'))

