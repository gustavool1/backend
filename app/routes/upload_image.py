from flask_pymongo import PyMongo
from flask import request

from app.routes.pymongo_config import pymongo_config 
def upload_image(app):
    @app.post("/")
    def upload():
        mongo = pymongo_config(app)
        if 'file' in request.files:
            file = request.files['file']
            mongo.save_file(file.filename, file)
            return {"file name": file.filename}

def get_image(app):
   @app.get("/get_file/<filename>")
   def get_file(filename):
    mongo = pymongo_config(app)
    return mongo.send_file(filename)