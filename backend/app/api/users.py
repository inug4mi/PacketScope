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

from app.models.user import User

from app.core.dependencies import get_current_user

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


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_my_profile(
    current_user: User = Depends(get_current_user)
):
    """
    Devuelve el usuario autenticado
    """
    return current_user