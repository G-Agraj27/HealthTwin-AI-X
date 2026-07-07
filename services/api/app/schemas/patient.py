from datetime import date

from pydantic import BaseModel


class PatientCreate(BaseModel):
    gender: str
    date_of_birth: date
    phone: str
    address: str
    blood_group: str
    emergency_contact: str


class PatientResponse(BaseModel):
    id: int
    user_id: int

    gender: str | None = None
    date_of_birth: date | None = None
    phone: str | None = None
    address: str | None = None
    blood_group: str | None = None
    emergency_contact: str | None = None

    class Config:
        from_attributes = True