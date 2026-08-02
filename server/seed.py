from app import app
from models import db, User, Note

with app.app_context():
    print("Deleting old data...")
    Note.query.delete()
    User.query.delete()

    print("Creating test users...")
    user1 = User(username="alice", password_hash="password123")
    user2 = User(username="bob", password_hash="password123")

    db.session.add_all([user1, user2])
    db.session.commit()