from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)

    start_date = Column(String(20), nullable=True)
    end_date = Column(String(20), nullable=True)

    description = Column(Text, nullable=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )

    candidate = relationship(
        "Candidate",
        back_populates="experiences",
    )