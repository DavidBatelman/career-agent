from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)

    institution = Column(String(255), nullable=False)
    degree = Column(String(255), nullable=True)
    field_of_study = Column(String(255), nullable=True)

    start_year = Column(Integer, nullable=True)
    end_year = Column(Integer, nullable=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )

    candidate = relationship(
        "Candidate",
        back_populates="education",
    )