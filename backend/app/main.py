from fastapi import FastAPI

app = FastAPI(
    title="NetSentinel API",
    description="Asset Discovery & Security Assessment Platform",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to NetSentinel API",
        "version": "0.1.0"
    }