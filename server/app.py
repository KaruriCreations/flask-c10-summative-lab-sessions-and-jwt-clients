import os
from flask import Flask, request, session
from flask_restful import Api, Resource
from flask_migrate import Migrate

from models import db, bcrypt, User, Note
from schemas import user_schema, note_schema, notes_schema

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY', 'vincent-maina-final-project5')

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

#fucntion to fetch currently logged in user
def get_current_user():
    user_id = session.get('user_id')
    if user_id:
        return User.query.get(user_id)
    return None

