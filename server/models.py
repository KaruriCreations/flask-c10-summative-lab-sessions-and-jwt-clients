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

    @property  #using a property getter to make it seem like _password_hash is a string
    def password_hash(self):
        raise AttributeError("Password cannot be accessed directly")
    
    @password_hash_setter  #using a setter to hash the password before storing it in the database
    def pasword_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8')
        ).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    
    

        


    