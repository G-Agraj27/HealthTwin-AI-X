from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.patient import PatientCreate, PatientResponse
from app.services.patient_service import (
    create_patient,
    get_patient,
    get_all_patients,
    update_patient,
    delete_patient,
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)


@router.post("/", response_model=PatientResponse)
def create_patient_api(
    patient: PatientCreate,
    db: Session = Depends(get_db),
):
    return create_patient(db, user_id=1, patient=patient)


@router.get("/", response_model=list[PatientResponse])
def get_patients_api(db: Session = Depends(get_db)):
    return get_all_patients(db)


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient_api(
    patient_id: int,
    db: Session = Depends(get_db),
):
    patient = get_patient(db, patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient_api(
    patient_id: int,
    patient: PatientCreate,
    db: Session = Depends(get_db),
):
    updated = update_patient(db, patient_id, patient)

    if not updated:
        raise HTTPException(status_code=404, detail="Patient not found")

    return updated


@router.delete("/{patient_id}")
def delete_patient_api(
    patient_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_patient(db, patient_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Patient not found")

    return {
        "message": "Patient deleted successfully"
    }