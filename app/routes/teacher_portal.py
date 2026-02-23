from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.session_deps import get_current_teacher

router = APIRouter(prefix="/teacher", tags=["Teacher Portal"])

@router.get("/me/courses")
def my_courses(current=Depends(get_current_teacher), db: Session = Depends(get_db)):
    # Return mock data for now - extend with real course assignments
    return {"courses": [{"code": "CS22403", "name": "Design and Analysis of Algorithms", "section": "A", "students": 45}]}

@router.get("/me/schedule")
def my_schedule(current=Depends(get_current_teacher), db: Session = Depends(get_db)):
    # Return mock data for now - extend with real schedule
    return {"schedule": [{"day": "Monday", "time": "09:00-10:00", "course": "CS22403", "room": "Lab-301"}]}