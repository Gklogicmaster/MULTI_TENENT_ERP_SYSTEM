from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Dict
import uuid

from app.database import get_db
from app.models.attendance import Attendance
from app.models.fees import Fees
from app.models.marks import Marks
from app.services.academic_service import AcademicService

router = APIRouter(prefix="/academic", tags=["Academic"])

# request schema
class AttendanceUpdate(BaseModel):
    student_id: str
    attendance: float

# response schema
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

@router.get("/{laid}")
def get_student_academic(laid: str, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.laid == laid).all()
    fees = db.query(Fees).filter(Fees.laid == laid).all()
    marks = db.query(Marks).filter(Marks.laid == laid).all()

    return {
        "laid": laid,
        "attendance": attendance,
        "fees": fees,
        "marks": marks
    }
