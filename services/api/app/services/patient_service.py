from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.schemas.patient import PatientCreate


def create_patient(db: Session, user_id: int, patient: PatientCreate):
    db_patient = Patient(
        user_id=user_id,
        gender=patient.gender,
        date_of_birth=patient.date_of_birth,
        phone=patient.phone,
        address=patient.address,
        blood_group=patient.blood_group,
        emergency_contact=patient.emergency_contact,
    )

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient


def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()


def get_all_patients(db: Session):
    return db.query(Patient).all()


def update_patient(db: Session, patient_id: int, patient: PatientCreate):
    db_patient = get_patient(db, patient_id)

    if not db_patient:
        return None

    db_patient.gender = patient.gender
    db_patient.date_of_birth = patient.date_of_birth
    db_patient.phone = patient.phone
    db_patient.address = patient.address
    db_patient.blood_group = patient.blood_group
    db_patient.emergency_contact = patient.emergency_contact

    db.commit()
    db.refresh(db_patient)

    return db_patient


def delete_patient(db: Session, patient_id: int):
    db_patient = get_patient(db, patient_id)

    if not db_patient:
        return None

    db.delete(db_patient)
    db.commit()

    return db_patient