from pydantic import BaseModel


class CandidateCreate(BaseModel):
    name: str
    email: str | None = None
    university: str | None = None
    degree: str | None = None
    graduation_year: int | None = None
    summary: str | None = None


class CandidateResponse(BaseModel):
    id: int
    name: str
    email: str | None = None
    university: str | None = None
    degree: str | None = None
    graduation_year: int | None = None
    summary: str | None = None

    class Config:
        from_attributes = True