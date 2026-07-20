from fastapi import FastAPI
from app.core.config import APP_NAME
from sqlalchemy import text
from app.db.database import engine

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

