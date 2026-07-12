from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.doctor import DoctorCreate, DoctorResponse
from app.services.doctor_service import (
    create_doctor,
    get_doctor,
    get_all_doctors,
    update_doctor,
    delete_doctor,
)

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"],
)


@router.post("/", response_model=DoctorResponse)
def create_doctor_api(
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
):
    return create_doctor(db, user_id=1, doctor=doctor)


@router.get("/", response_model=list[DoctorResponse])
def get_doctors_api(db: Session = Depends(get_db)):
    return get_all_doctors(db)


@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor_api(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    doctor = get_doctor(db, doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


@router.put("/{doctor_id}", response_model=DoctorResponse)
def update_doctor_api(
    doctor_id: int,
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
):
    updated = update_doctor(db, doctor_id, doctor)

    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return updated


@router.delete("/{doctor_id}")
def delete_doctor_api(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_doctor(db, doctor_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return {
        "message": "Doctor deleted successfully"
    }