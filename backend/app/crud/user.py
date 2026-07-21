from sqlalchemy.orm import Session
from app.models.user import User

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id():
    pass

def create_user():
    pass

def delete_user():
    pass