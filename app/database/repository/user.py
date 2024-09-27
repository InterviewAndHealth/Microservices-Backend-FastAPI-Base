from app.database import SessionLocal
from app.database.models import User


class UserRepository:
    def create(self, user: User):
        db = SessionLocal()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get(self, user_id):
        db = SessionLocal()
        return db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email):
        db = SessionLocal()
        return db.query(User).filter(User.email == email).first()
