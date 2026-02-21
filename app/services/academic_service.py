from app.domain.student import Student
from app.services.compliance_service import ComplianceService


class AcademicService:

    @staticmethod
    def update_attendance(db, student_id, new_attendance):
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return None

        student.attendance = new_attendance
        db.commit()

        # Trigger compliance check
        ComplianceService.check_student_compliance(db, student)

        return student

    @staticmethod
    def update_gpa(db, student_id, new_gpa):
        student = db.query(Student).filter(Student.id == student_id).first()

        if not student:
            return None

        student.cgpa = new_gpa
        db.commit()

        # Trigger compliance check
        ComplianceService.check_student_compliance(db, student)

        return student