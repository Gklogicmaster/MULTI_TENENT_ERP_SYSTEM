from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Dict
import uuid

from app.db.database import SessionLocal
from app.services.academic_service import AcademicService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Request Schema
class AttendanceUpdate(BaseModel):
    student_id: str
    attendance: float


# Response Schema
class MessageResponse(BaseModel):
    message: str


@router.put("/update-attendance", response_model=MessageResponse)
def update_attendance(data: AttendanceUpdate, db: Session = Depends(get_db)):

    # Validate UUID
    try:
        student_uuid = uuid.UUID(data.student_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid student UUID")

    student = AcademicService.update_attendance(
        db,
        student_uuid,
        data.attendance
    )

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Attendance updated successfully"}