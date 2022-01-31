from flask import request
import gridfs
# from app.routes.pymongo_config import pymongo_config 
def upload_image(app, mongo):
    @app.post("/")
    def upload():
        if 'file' in request.files:
            file = request.files['file']
            mongo.save_file(file.filename, file)
            return {"file name": file.filename}

def get_image(app, mongo):
   @app.get("/file/<filename>")
   def get_file(filename):
    return mongo.send_file(filename)