from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.session import Base


class AIChat(Base):
    __tablename__ = "ai_chat_history"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.id"))

    user_message = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    patient = relationship("Patient")