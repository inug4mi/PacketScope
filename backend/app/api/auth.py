from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.crud.auth import authenticate_user
from app.schemas.auth import LoginRequest

from app.core.security import create_access_token

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
    
    # if authenticated creates token by email
    access_token = create_access_token(
        subject=user.email
    )

    # if token made successful then logged
    return {
        "message": "Login successfull",
        "access_token": access_token,
        "token_type": "bearer"
    }
