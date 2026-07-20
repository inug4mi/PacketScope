from fastapi import FastAPI
from app.core.config import APP_NAME

app = FastAPI(
    title=APP_NAME,
    description="Asset Discovery & Security Assessment Platform",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {APP_NAME}!",
        "version": "0.1.0"
    }