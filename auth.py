from models import User
from db import SessionLocal
import bcrypt

def create_test_user():
    db = SessionLocal()
    user = db.query(User).filter(User.username == "testuser").first()
    if not user:
        hashed_pw = bcrypt.hashpw("testpass".encode("utf-8"), bcrypt.gensalt())
        new_user = User(username="testuser", password=hashed_pw.decode("utf-8"))
        db.add(new_user)
        db.commit()
        print("Test user created.")
    else:
        print("Test user already exists.")
    db.close()

