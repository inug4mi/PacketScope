from sqlalchemy.orm import Session

from app.core.security import verify_password
from app.crud.user import get_user_by_email


def authenticate_user(db: Session, email: str, password: str):

    # checks user exists by email
    user = get_user_by_email(db, email)
    if not user: return None

    # checks if password mathes
    password_match = verify_password(password, user.hashed_password)
    if not password_match: return None

    # authenticated
    return user