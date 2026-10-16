from fastapi import FastAPI
from app.database import engine, Base
from app.models import log 
from app.api.v1.endpoints.logs import router as logs_router

app = FastAPI(title="LogPulse API", version="1.0.0")

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(logs_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "LogPulse Engine is running"}