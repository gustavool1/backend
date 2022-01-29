from flask import Flask

from app.routes import init_app

def create_app():
    app = Flask(__name__)
    init_app(app)
    app.config["MONGO_URI"] ="mongodb+srv://gustavo:1234@cluster0.yrtgs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    return app