from flask import Flask
from flask_pymongo import PyMongo

from app.routes import init_app

def create_app():
    app = Flask(__name__)
    # app.config["MONGO_URI"] ="mongodb+srv://gustavo:1234@cluster0.yrtgs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    mongo = PyMongo(app, uri="mongodb+srv://gustavo:1234@cluster0.yrtgs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    init_app(app, mongo)
    return app