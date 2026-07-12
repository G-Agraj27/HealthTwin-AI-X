from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    specialization = Column(String, nullable=False)
    qualification = Column(String, nullable=True)
    experience = Column(Integer, nullable=True)

    phone = Column(String, nullable=True)
    consultation_fee = Column(Float, nullable=True)

    user = relationship("User")