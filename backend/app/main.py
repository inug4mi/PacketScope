from fastapi import FastAPI, Depends
from app.core.config import APP_NAME

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.database import engine
from app.db.database import SessionLocal
from app.db.database import get_db
from app.models.user import User

app = FastAPI(
    title=APP_NAME,
    description="Asset Discovery & Security Assessment Platform",
    version="0.1.0",
)

@app.on_event("startup")
def test_database_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("✅ Conexión exitosa con PostgreSQL")


@app.get("/")
def root():
    return {
        "message": f"Welcome to {APP_NAME}!",
        "version": "0.1.0"
    }


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at,
        }
        for user in users
    ]