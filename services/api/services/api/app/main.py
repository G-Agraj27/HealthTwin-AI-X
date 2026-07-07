from fastapi import FastAPI

from app.core.config import settings
from app.db.session import Base, engine
from app.models.user import User

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="HealthTwin AI X Backend API",
)


@app.get("/")
def root():
    return {
        "project": settings.APP_NAME,
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }