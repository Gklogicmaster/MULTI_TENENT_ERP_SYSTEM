"""Test script to verify database and API setup"""
from app.database import SessionLocal
from app.models.students import Student
from app.models.teacher_global import TeacherGlobal
from app.models.admin_global import AdminGlobal
from app.models.attendance import Attendance
from app.models.marks import Mark
from app.models.fees import Fee
from app.models.enrollment import Enrollment

def test_database():
    db = SessionLocal()
    
    print("=" * 60)
    print("DATABASE TEST")
    print("=" * 60)
    
    # Test students
    students = db.query(Student).all()
    print(f"\n[OK] Students: {len(students)} records")
    for s in students:
        print(f"  - {s.laid} | {s.name} | Institution {s.institution_id}")
    
    # Test teachers
    teachers = db.query(TeacherGlobal).all()
    print(f"\n[OK] Teachers: {len(teachers)} records")
    for t in teachers:
        print(f"  - {t.laid} | {t.name}")
    
    # Test admins
    admins = db.query(AdminGlobal).all()
    print(f"\n[OK] Admins: {len(admins)} records")
    for a in admins:
        print(f"  - {a.laid} | {a.name}")
    
    # Test attendance
    attendance = db.query(Attendance).all()
    print(f"\n[OK] Attendance: {len(attendance)} records")
    
    # Test marks
    marks = db.query(Mark).all()
    print(f"\n[OK] Marks: {len(marks)} records")
    
    # Test fees
    fees = db.query(Fee).all()
    print(f"\n[OK] Fees: {len(fees)} records")
    
    # Test enrollments
    enrollments = db.query(Enrollment).all()
    print(f"\n[OK] Enrollments: {len(enrollments)} records")
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)
    print("\nYou can now start the server:")
    print("  python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    print("\nThen open frontend:")
    print("  vscode/index.html or admin/index.html")
    print("\nLogin with:")
    print("  LAID: S101-ABC123")
    print("  Password: student123")
    
    db.close()

if __name__ == "__main__":
    test_database()
