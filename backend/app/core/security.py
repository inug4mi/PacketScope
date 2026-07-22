from datetime import datetime, timedelta, UTC

import jwt
from pwdlib import PasswordHash

from app.core.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """
    Genera un hash seguro de una contraseña.
    """
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Comprueba si una contraseña coincide con su hash.
    """
    return password_hash.verify(plain_password, hashed_password)


def create_access_token(subject: str) -> str:
    """
    Genera un JWT para el usuario autenticado
    """

    expire = datetime.now(UTC) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": subject,
        "exp": expire,
    }

    encoded_jwt = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return encoded_jwt
