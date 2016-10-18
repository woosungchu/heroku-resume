from flask import Blueprint, render_template, request , session, redirect , url_for, make_response
from flask.views import MethodView
from tumblelog.models import Post
from flask_mongoengine.wtf import model_form
from mongoengine.queryset import Q
import json

ROOT = '/tumblelog/'
tumblelog = Blueprint('tumblelog',__name__,template_folder='_templates'+ROOT)
PER_PAGE = 10
STACKS = ['Flask','MongoDB','MongoEngine','jQuery']

class ListView(MethodView):
    
    form = model_form(Post, exclude=['created_at','author','id'])
    
    def get_context(self):
        """
        1. select Posts which hidden attribute is null or False(Not private post)
        2. select Posts which author is user in session where its hidden attribute is True or False
        """
        user = session.get('SESSION_USER',None)
        posts = Post.objects.filter( 
                    Q(hidden=None) | 
                    Q(hidden=False) | 
                    Q(hidden=True,author=user)
                ).limit(PER_PAGE)
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
            post.save(validate=False) # To ignore NullException in ObjectIdField - should figure out better solution
            
            return redirect(url_for('tumblelog.list'))
        return render_template(ROOT+'list.html', **context)

class MorePage(MethodView):
    
    def get(self,page):
        skip = int(page) if page != None else 0 
        user = session.get('SESSION_USER',None)
        posts = Post.objects.filter( 
                    Q(hidden=None) | 
                    Q(hidden=False) | 
                    Q(hidden=True,author=user)
                ).skip(skip).limit(PER_PAGE)
        
        response = make_response(posts.to_json())
        response.content_type = 'application/json'
        return response
        
class DetailView(MethodView):
    
    def get_context(self,id):
        post = Post.objects.get_or_404(id=id)
    
        context = {
            "post":post,
            'stack':STACKS
        }
        return context

    def get(self, id):
        context = self.get_context(id)
        return render_template(ROOT+'detail.html',  **context)

tumblelog.add_url_rule(ROOT,view_func= ListView.as_view('list'))
tumblelog.add_url_rule(ROOT+'<id>/',view_func= DetailView.as_view('detail'))
tumblelog.add_url_rule(ROOT+'page/<page>/',view_func= MorePage.as_view('page'))
