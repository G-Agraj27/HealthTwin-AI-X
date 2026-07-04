from fastapi import FastAPI

app = FastAPI(
    title="HealthTwin AI X API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to HealthTwin AI X API 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }