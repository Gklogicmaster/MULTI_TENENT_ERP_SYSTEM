from app.domain.student import Student
from app.domain.compliance import ComplianceLog


class ComplianceService:

    @staticmethod
    def check_student_compliance(db, student: Student):

        alerts_to_check = [
            {
                "condition": student.attendance is not None and student.attendance < 75,
                "message": "Attendance below 75%"
            },
            {
                "condition": student.cgpa is not None and student.cgpa < 5,
                "message": "CGPA below 5"
            }
        ]

        for rule in alerts_to_check:
            if rule["condition"]:

                existing = db.query(ComplianceLog).filter(
                    ComplianceLog.user_id == student.user_id,
                    ComplianceLog.message == rule["message"],
                    ComplianceLog.resolved == False
                ).first()

                if not existing:
                    log = ComplianceLog(
                        user_id=student.user_id,
                        message=rule["message"]
                    )
                    db.add(log)

        db.commit()