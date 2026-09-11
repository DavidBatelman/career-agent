from fastapi import FastAPI

from app.database import Base, engine
from app.models import (
    Candidate,
    Skill,
    Experience,
    Project,
    Education,
)
from app.api.routes.candidate import router as candidate_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Career Agent",
    description="AI-powered job matching and career optimization platform",
    version="0.1.0",
)


app.include_router(candidate_router)


@app.get("/")
def root():
    return {
        "name": "AI Career Agent",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}