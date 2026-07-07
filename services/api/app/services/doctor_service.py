from sqlalchemy.orm import Session

from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate


def create_doctor(db: Session, user_id: int, doctor: DoctorCreate):
    db_doctor = Doctor(
        user_id=user_id,
        specialization=doctor.specialization,
        qualification=doctor.qualification,
        experience=doctor.experience,
        phone=doctor.phone,
        consultation_fee=doctor.consultation_fee,
    )

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return db_doctor


def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()


def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def update_doctor(db: Session, doctor_id: int, doctor: DoctorCreate):
    db_doctor = get_doctor(db, doctor_id)

    if not db_doctor:
        return None

    db_doctor.specialization = doctor.specialization
    db_doctor.qualification = doctor.qualification
    db_doctor.experience = doctor.experience
    db_doctor.phone = doctor.phone
    db_doctor.consultation_fee = doctor.consultation_fee

    db.commit()
    db.refresh(db_doctor)

    return db_doctor


def delete_doctor(db: Session, doctor_id: int):
    db_doctor = get_doctor(db, doctor_id)

    if not db_doctor:
        return None

    db.delete(db_doctor)
    db.commit()

    return db_doctor