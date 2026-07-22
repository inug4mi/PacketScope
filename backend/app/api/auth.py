from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.crud.auth import authenticate_user
from app.schemas.auth import LoginRequest

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db=db,
        email=credentials.email,
        password=credentials.password
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    return {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }