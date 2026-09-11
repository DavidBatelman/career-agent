from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    category = Column(String(100), nullable=True)
    proficiency = Column(String(50), nullable=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )

    candidate = relationship(
        "Candidate",
        back_populates="skills",
    )