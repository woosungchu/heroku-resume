from flask import Blueprint, redirect, url_for, render_template, request, session, flash
from flask.views import MethodView
from user.models import User
from flask_mongoengine.wtf import model_form
from resume import flask_bcrypt

user = Blueprint('user',__name__,template_folder='_templates')
ROOT = '/user/'
STACKS = ['Flask','MongoDB','MongoEngine','jQuery','Flask-Bcrypt']

class NewAccount(MethodView):
    form = model_form(User, exclude=['created_at'], field_args={'password': {'password':True}})
    
    def get_context(self):
        form = self.form(request.form)
         
        context = {
            'form':form,
            "stack" : STACKS 
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
            user.password = str(flask_bcrypt.generate_password_hash(user.password),'utf-8')
            user.save()
            return redirect(url_for('user.login'))
        
        flash('Your request failed to pass','newAccount')
        return redirect(url_for('user.new'))

class Login(MethodView):
    form = model_form(User, exclude=['created_at','name'], field_args={'password': {'password':True}})
    def get_context(self):
        form = self.form(request.form)
        context = {
            'form':form,
            "stack" : STACKS 
        }
        return context
    
    def get(self):
        context = self.get_context()
        return render_template(ROOT+'login.html',**context)
    
    def post(self):
        context = self.get_context()
        form = context.get('form') 

        reqUser = User()
        form.populate_obj(reqUser)
        try:
            user = User.objects.get(email=reqUser.email)
                
            print(user)
            if user and flask_bcrypt.check_password_hash(user.password,str.encode(reqUser.password)):
                session_user = user
                session['SESSION_USER'] = session_user
                #flash("login success")
                return redirect(url_for('index.index'))
        except User.DoesNotExist:
            pass
        flash("login failed",'login') 
        return redirect(url_for('user.login'))
        
class Logout(MethodView):
    def get(self):
        session['SESSION_USER'] = None
        return redirect(url_for('index.index'))

user.add_url_rule(ROOT+'new/',view_func= NewAccount.as_view('new'))
user.add_url_rule(ROOT+'login/',view_func= Login.as_view('login'))
user.add_url_rule(ROOT+'/logout',view_func= Logout.as_view('logout'))
