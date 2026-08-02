from app import app
from models import db, User, Note

with app.app_context():
    print("Deleting old data...")
    Note.query.delete()
    User.query.delete()

    print("Creating test users...")
    user1 = User(username="alice")
    user1.password_hash = "password123"

    user2 = User(username="bob")
    user2.password_hash = "password123"

    db.session.add_all([user1, user2])
    db.session.commit()

    print("Creating test notes...")
    n1 = Note(title="Alice's Note 1", content="Study Flask-RESTful", user_id=user1.id)
    n2 = Note(title="Alice's Note 2", content="Buy groceries", user_id=user1.id)
    n3 = Note(title="Bob's Note 1", content="Workout plan", user_id=user2.id)

    db.session.add_all([n1, n2, n3])
    db.session.commit()

    print("Seeding completed successfully!")