"""Initialize database with demo data for 2 institutions"""
import uuid
from app.database import SessionLocal, engine, Base
from app.models.students import Student
from app.models.teacher_global import TeacherGlobal
from app.models.admin_global import AdminGlobal
from app.models.attendance import Attendance
from app.models.marks import Mark
from app.models.fees import Fee
from app.models.enrollment import Enrollment

def generate_laid():
    return f"EDU-{str(uuid.uuid4())[:8]}"

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Generate LAIDs
    s1_laid = generate_laid()
    s2_laid = generate_laid()
    s3_laid = generate_laid()
    t1_laid = generate_laid()
    t2_laid = generate_laid()
    a1_laid = generate_laid()
    a2_laid = generate_laid()
    
    # Institution 101 - Government Engineering College
    s1 = Student(laid=s1_laid, institution_id=101, name="Arun Kumar", branch="CSE", 
                 mobile="9876543210", email="arun@gec.in", gender="Male", password="student123")
    s2 = Student(laid=s2_laid, institution_id=101, name="Priya Reddy", branch="CSE",
                 mobile="9876543211", email="priya@gec.in", gender="Female", password="student123")
    
    t1 = TeacherGlobal(laid=t1_laid, name="Dr. Priya Sharma", qualification="PhD", age=35,
                       mobile="9876543220", email="priya.sharma@gec.in", gender="Female", password="teacher123")
    
    a1 = AdminGlobal(laid=a1_laid, name="Admin GEC", email="admin@gec.in", password="admin123")
    
    # Institution 102 - Tech Institute
    s3 = Student(laid=s3_laid, institution_id=102, name="Rahul Singh", branch="ECE",
                 mobile="9876543212", email="rahul@tech.in", gender="Male", password="student123")
    
    t2 = TeacherGlobal(laid=t2_laid, name="Dr. Rajesh Kumar", qualification="PhD", age=40,
                       mobile="9876543221", email="rajesh@tech.in", gender="Male", password="teacher123")
    
    a2 = AdminGlobal(laid=a2_laid, name="Admin Tech", email="admin@tech.in", password="admin123")
    
    db.add_all([s1, s2, s3, t1, t2, a1, a2])
    
    # Attendance for first student
    att1 = Attendance(laid=s1_laid, institution_id=101, course_code="CS22403", status="Present", date="2026-02-18")
    att2 = Attendance(laid=s1_laid, institution_id=101, course_code="CS22404", status="Present", date="2026-02-18")
    db.add_all([att1, att2])
    
    # Marks
    m1 = Mark(laid=s1_laid, institution_id=101, course_code="CS22403", exam_type="Internal 1", marks=44, max_marks=50)
    m2 = Mark(laid=s1_laid, institution_id=101, course_code="CS22404", exam_type="Internal 1", marks=41, max_marks=50)
    db.add_all([m1, m2])
    
    # Fees
    f1 = Fee(laid=s1_laid, institution_id=101, total_amount=25000, paid_amount=15000, due_amount=10000, semester="Spring 2026")
    db.add(f1)
    
    # Enrollments
    e1 = Enrollment(laid=s1_laid, institution_id=101, course_code="CS22403", course_name="Design and Analysis of Algorithms", status="active")
    e2 = Enrollment(laid=s1_laid, institution_id=101, course_code="CS22404", course_name="Operating Systems", status="active")
    db.add_all([e1, e2])
    
    db.commit()
    print("[SUCCESS] Database initialized with demo data for 2 institutions!")
    print("\nDemo Credentials (EDU-format LAIDs):")
    print("\nInstitution 101 (GEC):")
    print(f"  Student: {s1_laid} / student123")
    print(f"  Student: {s2_laid} / student123")
    print(f"  Teacher: {t1_laid} / teacher123")
    print(f"  Admin: {a1_laid} / admin123")
    print("\nInstitution 102 (Tech):")
    print(f"  Student: {s3_laid} / student123")
    print(f"  Teacher: {t2_laid} / teacher123")
    print(f"  Admin: {a2_laid} / admin123")
    
    db.close()

if __name__ == "__main__":
    init_db()
