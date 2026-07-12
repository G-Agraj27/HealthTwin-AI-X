from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    appointment_date = Column(DateTime, nullable=False)
    reason = Column(String, nullable=True)
    status = Column(String, default="Scheduled")

    patient = relationship("Patient")
    doctor = relationship("Doctor")