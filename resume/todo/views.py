from flask import Flask, render_template, url_for, json, request, Blueprint
from flask.views import MethodView
from bson import ObjectId,json_util
from resume import db_pymongo
import json, os

ROOT = '/todo/'
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
        items =[]
        for item in todos.find():
            item['id'] = str(item['_id'])
            del item['_id']
            items.append(item)
        return json_util.dumps(list(items), default=json_util.default)
    
    def post(self):
        todo = json_util.loads(request.data.decode('utf-8'))
        todos.save(todo)
        return json_util.dumps(todo)
    
    def put(self,id):
        todo = json_util.loads(request.data.decode('utf-8'))
        todo['_id']=ObjectId(todo['id'])
        del todo['id']
        todos.save(todo)
        return json_util.dumps(todo)
    
    def delete(self,id):
        todos.remove(ObjectId(id))
        return ""

    @classmethod
    def register(cls,todo):
        url = '/rest'+ROOT
        f=cls.as_view('todo_api')
        todo.add_url_rule(url,view_func=f,methods=['GET'])
        todo.add_url_rule(url,view_func=f,methods=['POST'])
        todo.add_url_rule(url+'<id>',view_func=f,methods=['PUT','DELETE'])
TodoAPI.register(todo)
