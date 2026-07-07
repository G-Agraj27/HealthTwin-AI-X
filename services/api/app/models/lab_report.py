from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.session import Base


class LabReport(Base):
    __tablename__ = "lab_reports"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.id"))

    report_name = Column(String, nullable=False)
    report_type = Column(String, nullable=False)
    file_path = Column(String, nullable=True)

    ai_summary = Column(Text, nullable=True)

    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

    patient = relationship("Patient")