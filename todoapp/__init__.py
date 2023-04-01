from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api


app = Flask(__name__)
app.debug=True
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{Path(__file__).parent.parent.absolute().joinpath('todo.db')}"
db.init_app(app=app)
ma = Marshmallow(app)
api = Api(app)


from todoapp.views import *

with app.app_context():
    db.create_all()