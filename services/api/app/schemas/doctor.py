from pydantic import BaseModel


class DoctorCreate(BaseModel):
    specialization: str
    qualification: str
    experience: int
    phone: str
    consultation_fee: float


class DoctorResponse(BaseModel):
    id: int
    user_id: int

    specialization: str
    qualification: str
    experience: int
    phone: str
    consultation_fee: float

    class Config:
        from_attributes = True