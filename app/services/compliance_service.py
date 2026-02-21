from app.domain.student import Student
from app.domain.compliance import ComplianceLog


class ComplianceService:

    @staticmethod
    def check_student_compliance(db, student: Student):
        alerts = []

        # Attendance rule
        if student.attendance is not None and student.attendance < 75:
            alerts.append("Attendance below 75%")

        # GPA rule
        if student.cgpa is not None and student.cgpa < 5:
            alerts.append("CGPA below 5")

        for alert in alerts:
            log = ComplianceLog(
                user_id=student.user_id,
                message=alert
            )
            db.add(log)

        db.commit()

        return alerts