from flask import Flask, render_template, url_for, json, request, Blueprint
from flask.views import MethodView
from pymongo import MongoClient
from bson.objectid import ObjectId
import json

ROOT = '/todo/'
REST_URL = '/rest'+ROOT 
todo = Blueprint('todo',__name__,template_folder='_templates'+ROOT)
db  = MongoClient('mongodb://admin:admin@ds027425.mlab.com:27425/heroku_mr51rc25')
coll = db['heroku_mr51rc25']
todos = coll['todo']
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
        pass
    
    def post(self):
        pass
    
    def put(self):
        pass
    
    def delete(self):
        pass

    @classmethod
    def register(cls,todo):
        url = '/rest'+ROOT
        f=cls.as_view('todo_api')
        todo.add_url_rule(url,view_func=f,methods=['GET'])
        todo.add_url_rule(url,view_func=f,methods=['POST'])
        todo.add_url_rule(url+'<id>/',view_func=f,methods=['PUT','DELETE'])
TodoAPI.register(todo)
"""
@app.route(ROOT+'/')
def hello_world():
    return render_template('index.html')

@app.route(ROOT+'/todos')
def list_todos():
    return json_dump(list(todos.find()))
    
@app.route(ROOT+'/todos',  methods=['POST'])
def new_todo():
    todo = json_load(request.data)
    todos.save(todo)
    return json_dump(todo)

@app.route(ROOT+'/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = json_load(request.data)
    todos.save(todo)
    return json_dump(todo)

@app.route(ROOT+'/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos.remove(ObjectId(todo_id))
    return ""

"""