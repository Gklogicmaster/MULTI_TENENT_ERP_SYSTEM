"""Comprehensive System Check - Verify everything works"""
import sys
import os

print("="*70)
print("ERP SYSTEM - COMPREHENSIVE CHECK")
print("="*70)

errors = []
warnings = []

# Test 1: Check imports
print("\n[1/6] Checking imports...")
try:
    from app.main import app
    from app.routes import student_portal, teacher_portal, admin_portal, auth_session
    from app.models.students import Student
    from app.models.teacher_global import TeacherGlobal
    from app.models.admin_global import AdminGlobal
    print("  [OK] All imports successful")
except Exception as e:
    errors.append(f"Import error: {e}")
    print(f"  [ERROR] {e}")

# Test 2: Check database
print("\n[2/6] Checking database...")
try:
    from app.database import SessionLocal
    from app.models.students import Student
    from app.models.attendance import Attendance
    from app.models.marks import Mark
    from app.models.fees import Fee
    from app.models.enrollment import Enrollment
    
    db = SessionLocal()
    
    students = db.query(Student).all()
    teachers = db.query(TeacherGlobal).all()
    admins = db.query(AdminGlobal).all()
    attendance = db.query(Attendance).all()
    marks = db.query(Mark).all()
    fees = db.query(Fee).all()
    enrollments = db.query(Enrollment).all()
    
    print(f"  [OK] Students: {len(students)}")
    print(f"  [OK] Teachers: {len(teachers)}")
    print(f"  [OK] Admins: {len(admins)}")
    print(f"  [OK] Attendance: {len(attendance)}")
    print(f"  [OK] Marks: {len(marks)}")
    print(f"  [OK] Fees: {len(fees)}")
    print(f"  [OK] Enrollments: {len(enrollments)}")
    
    if len(students) == 0:
        errors.append("No students in database")
    
    db.close()
except Exception as e:
    errors.append(f"Database error: {e}")
    print(f"  [ERROR] {e}")

# Test 3: Check credentials
print("\n[3/6] Checking demo credentials...")
try:
    db = SessionLocal()
    
    # Check S101-ABC123
    s1 = db.query(Student).filter(Student.laid == 'S101-ABC123').first()
    if s1 and s1.password == 'student123':
        print("  [OK] S101-ABC123 / student123")
    else:
        errors.append("S101-ABC123 credentials incorrect")
    
    # Check T101-XYZ789
    t1 = db.query(TeacherGlobal).filter(TeacherGlobal.laid == 'T101-XYZ789').first()
    if t1 and t1.password == 'teacher123':
        print("  [OK] T101-XYZ789 / teacher123")
    else:
        errors.append("T101-XYZ789 credentials incorrect")
    
    # Check A101-ADMIN1
    a1 = db.query(AdminGlobal).filter(AdminGlobal.laid == 'A101-ADMIN1').first()
    if a1 and a1.password == 'admin123':
        print("  [OK] A101-ADMIN1 / admin123")
    else:
        errors.append("A101-ADMIN1 credentials incorrect")
    
    db.close()
except Exception as e:
    errors.append(f"Credentials check error: {e}")
    print(f"  [ERROR] {e}")

# Test 4: Check frontend files
print("\n[4/6] Checking frontend files...")
frontend_files = [
    ("vscode/index.html", "Landing page"),
    ("vscode/login.html", "Login page"),
    ("vscode/student.html", "Student portal"),
    ("vscode/apiService.js", "API service"),
    ("admin/index.html", "Admin landing page"),
    ("admin/login.html", "Admin login page"),
]

for file_path, desc in frontend_files:
    full_path = os.path.join("..", "..", file_path)
    if os.path.exists(full_path):
        print(f"  [OK] {desc}: {file_path}")
    else:
        warnings.append(f"Missing: {file_path}")
        print(f"  [WARN] Missing: {file_path}")

# Test 5: Check API routes
print("\n[5/6] Checking API routes...")
try:
    from app.main import app
    routes = [r.path for r in app.routes]
    
    required_routes = [
        "/auth/login",
        "/auth/logout",
        "/student/me/attendance",
        "/student/me/marks",
        "/student/me/fees",
        "/student/me/courses",
        "/teacher/me/courses",
        "/teacher/me/schedule",
        "/admin/me/stats"
    ]
    
    for route in required_routes:
        if route in routes:
            print(f"  [OK] {route}")
        else:
            errors.append(f"Missing route: {route}")
            print(f"  [ERROR] Missing: {route}")
            
except Exception as e:
    errors.append(f"Route check error: {e}")
    print(f"  [ERROR] {e}")

# Test 6: Check CORS
print("\n[6/6] Checking CORS configuration...")
try:
    from app.main import app
    has_cors = any('cors' in str(m).lower() for m in app.user_middleware)
    if has_cors:
        print("  [OK] CORS middleware enabled")
    else:
        warnings.append("CORS middleware not found")
        print("  [WARN] CORS middleware not found")
except Exception as e:
    warnings.append(f"CORS check error: {e}")
    print(f"  [WARN] {e}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)

if len(errors) == 0 and len(warnings) == 0:
    print("\n[SUCCESS] All checks passed! System is ready to run.")
    print("\nNext steps:")
    print("  1. Start server: python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    print("  2. Open frontend: vscode/index.html or admin/index.html")
    print("  3. Login with: S101-ABC123 / student123")
    sys.exit(0)
elif len(errors) == 0:
    print(f"\n[OK] System is functional with {len(warnings)} warnings")
    for w in warnings:
        print(f"  - {w}")
    sys.exit(0)
else:
    print(f"\n[ERROR] Found {len(errors)} errors:")
    for e in errors:
        print(f"  - {e}")
    if len(warnings) > 0:
        print(f"\nAlso found {len(warnings)} warnings:")
        for w in warnings:
            print(f"  - {w}")
    print("\nPlease fix errors before running the system.")
    sys.exit(1)
