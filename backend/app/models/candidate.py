from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=True)

    university = Column(String(255), nullable=True)
    degree = Column(String(255), nullable=True)
    graduation_year = Column(Integer, nullable=True)

    summary = Column(Text, nullable=True)

    skills = relationship(
        "Skill",
        back_populates="candidate",
        cascade="all, delete-orphan",
    )

    experiences = relationship(
        "Experience",
        back_populates="candidate",
        cascade="all, delete-orphan",
    )

    projects = relationship(
        "Project",
        back_populates="candidate",
        cascade="all, delete-orphan",
    )

    education = relationship(
        "Education",
        back_populates="candidate",
        cascade="all, delete-orphan",
    )