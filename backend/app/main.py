from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import APP_NAME
from app.db.database import engine

from app.api.users import router as users_router
from app.api.auth import router as auth_router

app = FastAPI(
    title=APP_NAME,
    description="Asset Discovery & Security Assessment Platform",
    version="0.2.0",
)


@app.on_event("startup")
def test_database_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("✅ PostgreSQL connection successful")


@app.get("/")
def root():
    return {
        "message": f"Welcome to {APP_NAME}!",
        "version": "0.2.0"
    }


from app.core.security import (
    create_access_token,
    decode_access_token,
)

@app.get("/test-token")
def test_token():
    token = create_access_token(
        "inug4mi@example.com"
    )

    return {
        "token": token,
    }


@app.get("/decode-test")
def decode_test():
    token = create_access_token(
        "inug4mi@example.com"
    )

    payload = decode_access_token(token)
    return {
        "token": token,
        "payload": payload,
    }

app.include_router(users_router)
app.include_router(auth_router)