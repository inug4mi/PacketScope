from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.crud.auth import authenticate_user

from app.core.security import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Autentica un usuario mediante email y contraseña 
    y devuelve un JWT
    """
    # tries to authenticate
    user = authenticate_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )

    if user is None: # authentication failed
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        ) 
    
    # authenticated, then creates token by email
    access_token = create_access_token(
        subject=user.email
    )

    # if token is made successfully then logged
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
