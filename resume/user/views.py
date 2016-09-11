from flask import Blueprint, redirect, url_for, render_template, request, session, flash
from flask.views import MethodView
from user.models import User
from flask_mongoengine.wtf import model_form

user = Blueprint('user',__name__,template_folder='_templates')
ROOT = '/user/'

class NewAccount(MethodView):
    form = model_form(User, exclude=['created_at'], field_args={'password': {'password':True}})
    
    def get_context(self):
        form = self.form(request.form)
         
        context = {
            'form':form
         }
        return context
    
    def get(self):
        context = self.get_context()
        return render_template(ROOT+'new.html', **context)
    
    def post(self):
        context = self.get_context()
        form = context.get('form')
        
        if form.validate():
            user = User()
            form.populate_obj(user)
            #user.save()
            print(user)
            #error
            return redirect(url_for('user.login'))
        
        flash('Your request failed to pass','error')
        return redirect(url_for('user.new'))

class Login(MethodView):
    form = model_form(User, exclude=['created_at','name'], field_args={'password': {'password':True}})
    def get_context(self):
        form = self.form(request.form)
        
        context = {
            'form':form
        }
        return context
    
    def get(self):
        context = self.get_context()
        return render_template(ROOT+'login.html',**context)
        
user.add_url_rule(ROOT+'new/',view_func= NewAccount.as_view('new'))
user.add_url_rule(ROOT+'login/',view_func= Login.as_view('login'))
#user.add_url_rule(ROOT+'/logout',view_func= Logout.as_view('logout'))
