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

#auth endpoints
class Signup(Resource):
    def post(self):
        data = request.get_json()
        errors = user_schema.validate(data)
        if errors:
            return errors, 400
        if User.query.filter_by(username=data['username']).first():
            return {'error': 'Username already exists'}, 400
        user = User(username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        return user_schema.dump(user), 201