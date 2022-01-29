from flask_pymongo import PyMongo
def pymongo_config(app):
    return PyMongo(app)