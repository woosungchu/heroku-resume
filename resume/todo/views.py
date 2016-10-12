from flask import Flask, render_template, url_for, json, request, Blueprint
from flask.views import MethodView
from bson import ObjectId,json_util
from resume import db_pymongo
import json, os

ROOT = '/todo/'
REST_URL = '/rest'+ROOT 
todo = Blueprint('todo',__name__,template_folder='_templates'+ROOT)
todos = db_pymongo['heroku_mr51rc25']['todo']
STACKS = ['Flask','MongoDB','RESTful-API','jQuery']

class TodoView(MethodView):
    
    def get_context(self):
        
        context = {
            'stack':STACKS
        }
        
        return context
    
    def get(self):
        context = self.get_context()
        return render_template(ROOT+'list.html',**context)
    
#    @classmethod
#    def register(cls):
#        todo.add_url_rule(ROOT,view_func=cls.as_view('list'))
todo.add_url_rule(ROOT,view_func=TodoView.as_view('list'))

class TodoAPI(MethodView):
    
    def get(self):
        return json_util.dumps(todos.find())
    
    def post(self):
        todo = json_util.loads(request.data.decode('utf-8'))
        todos.save(todo)
        return json_util.dumps(todo)
    
    def put(self):
        todo = json_util.loads(request.data.decode('utf-8'))
        todos.save(todo)
        return json_util.dumps(todo)
    
    def delete(self):
        todos.remove(ObjectId(todo_id))
        return ""

    @classmethod
    def register(cls,todo):
        url = '/rest'+ROOT
        f=cls.as_view('todo_api')
        todo.add_url_rule(url,view_func=f,methods=['GET'])
        todo.add_url_rule(url,view_func=f,methods=['POST'])
        todo.add_url_rule(url+'<id>/',view_func=f,methods=['PUT','DELETE'])
TodoAPI.register(todo)
