from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.session_deps import get_current_admin
from app.models.students import Student
from app.models.teacher_global import TeacherGlobal

router = APIRouter(prefix="/admin", tags=["Admin Portal"])

@router.get("/me/stats")
def my_stats(current=Depends(get_current_admin), db: Session = Depends(get_db)):
    institution_id = current["institution_id"]
    
    total_students = db.query(Student).filter(Student.institution_id == institution_id).count()
    total_teachers = db.query(TeacherGlobal).count()
    
    return {
        "stats": {
            "totalStudents": total_students,
            "totalFaculty": total_teachers,
            "totalCourses": 120,
            "activeAdmissions": 85
        }
    }