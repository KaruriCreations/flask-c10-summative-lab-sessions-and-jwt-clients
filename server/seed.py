from app import app
from models import db, User, Note

with app.app_context():
    print("Deleting old data...")
    Note.query.delete()
    User.query.delete()