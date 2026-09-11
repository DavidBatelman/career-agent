from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    github_url = Column(String(500), nullable=True)
    demo_url = Column(String(500), nullable=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )

    candidate = relationship(
        "Candidate",
        back_populates="projects",
    )