from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import validates

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, UNIQUE=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    #relationship to note model
    notes = db.relationship('Note', backref='user', cascade='all, delete-orphan')

    


    