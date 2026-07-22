from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.crud.user import (
    get_all_users,
    create_user,
)

from app.schemas.user import (
    UserCreate,
    UserResponse
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.post(
    "/",
    response_model=UserResponse,
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
): return create_user(db, user)
