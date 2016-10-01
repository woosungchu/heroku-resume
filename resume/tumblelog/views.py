from flask import Blueprint, render_template, request , session, redirect , url_for
from flask.views import MethodView
from tumblelog.models import Post
from flask_mongoengine.wtf import model_form
from mongoengine.queryset import Q


ROOT = '/tumblelog/'
tumblelog = Blueprint('tumblelog',__name__,template_folder='_templates'+ROOT)
STACKS = ['Flask','MongoDB','MongoEngine','jQuery']

class ListView(MethodView):
    
    form = model_form(Post, exclude=['created_at','author'])
    
    def get_context(self):
        user = session.get('SESSION_USER',None)
        posts = Post.objects.filter( Q(hidden=False) | Q(hidden=True,author=user))
        form = self.form(request.form)
        
        context = {
            "posts" : posts,
            "form" : form,
            "stack" : STACKS 
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
            post.author = session.get('SESSION_USER',None)
            post.save()
            
            return redirect(url_for('tumblelog.list'))
        return render_template(ROOT+'list.html', **context)
        
class DetailView(MethodView):
    
    def get_context(self,title):
        post = Post.objects.get_or_404(title=title)
    
        context = {
            "post":post,
            'stack':STACKS
        }
        return context

    def get(self, title):
        post = Post.objects.get_or_404(title=title)
        return render_template(ROOT+'detail.html', post=post)

tumblelog.add_url_rule(ROOT,view_func= ListView.as_view('list'))
tumblelog.add_url_rule(ROOT+'<title>/',view_func= DetailView.as_view('detail'))
