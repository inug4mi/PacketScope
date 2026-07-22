from sqlalchemy.orm import Session
from sqlalchemy import asc

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


def get_all_users(db: Session):
    try:
        return db.query(User).order_by(asc(User.id)).all()
    except Exception as e:
        print(f"Error detectado: {e}")
        raise e

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first(    )

def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user