"""Quick login test"""
from app.database import SessionLocal
from app.models.students import Student

db = SessionLocal()

# Test S101-ABC123
student = db.query(Student).filter(
    Student.laid == 'S101-ABC123',
    Student.institution_id == 101
).first()

if student:
    print(f"[OK] Found student: {student.name}")
    print(f"[OK] LAID: {student.laid}")
    print(f"[OK] Password: {student.password}")
    print(f"[OK] Institution: {student.institution_id}")
    
    if student.password == 'student123':
        print("\n[SUCCESS] Login credentials are correct!")
        print("\nYou can now:")
        print("1. Start server: python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
        print("2. Open: vscode/index.html")
        print("3. Login with: S101-ABC123 / student123")
    else:
        print(f"\n[ERROR] Password mismatch: {student.password}")
else:
    print("[ERROR] Student not found!")

db.close()
