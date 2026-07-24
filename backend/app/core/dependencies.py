from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.oauth2 import oauth2_scheme
from app.core.security import decode_access_token

from app.db.database import get_db

from app.crud.auth import get_user_by_email

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):  
    """
    Obtiene el usuario autenticado a partir del JWT
    """

    payload = decode_access_token(token)

    if payload is None: # Token no valido
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    email = payload.get("sub")

    if email is None: # No hay email basado en este token
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )
    
    # obten nombre de usuario basado en el email
    user = get_user_by_email(
        db=db,
        email=email
    )

    if user is None: # No existe usuario con este email
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    # Si existe un nombre de usuario basado en este email
    return user
        
    