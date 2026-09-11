from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateResponse


router = APIRouter(
    prefix="/api/candidate",
    tags=["Candidate"],
)


@router.get("/", response_model=CandidateResponse)
def get_candidate(db: Session = Depends(get_db)):
    candidate = db.query(Candidate).first()

    if candidate is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate profile not found",
        )

    return candidate


@router.post("/", response_model=CandidateResponse, status_code=201)
def create_candidate(
    candidate_data: CandidateCreate,
    db: Session = Depends(get_db),
):
    existing_candidate = db.query(Candidate).first()

    if existing_candidate is not None:
        raise HTTPException(
            status_code=409,
            detail="Candidate profile already exists",
        )

    candidate = Candidate(
        name=candidate_data.name,
        email=candidate_data.email,
        university=candidate_data.university,
        degree=candidate_data.degree,
        graduation_year=candidate_data.graduation_year,
        summary=candidate_data.summary,
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate