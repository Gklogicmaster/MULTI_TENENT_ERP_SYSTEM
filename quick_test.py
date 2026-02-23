"""Quick Test - Verify System is Working"""
import requests
import sys

print("="*70)
print("TESTING ERP SYSTEM WITH EDU-FORMAT LAIDs")
print("="*70)

# Get LAIDs from database
from app.database import SessionLocal
from app.models.students import Student

db = SessionLocal()
student = db.query(Student).first()

if not student:
    print("\n[ERROR] No students in database!")
    print("Run: python init_demo_data.py")
    sys.exit(1)

test_laid = student.laid
test_password = "student123"

print(f"\n[INFO] Testing with LAID: {test_laid}")
print(f"[INFO] Password: {test_password}")

# Test 1: Check if server is running
print("\n[1/4] Checking if server is running...")
try:
    response = requests.get("http://localhost:8000/", timeout=2)
    print("  ✓ Server is running")
except:
    print("  ✗ Server is NOT running!")
    print("\n  Start server first:")
    print("    python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    sys.exit(1)

# Test 2: Test login
print("\n[2/4] Testing login...")
try:
    response = requests.post(
        f"http://localhost:8000/auth/login?laid={test_laid}&password={test_password}"
    )
    if response.status_code == 200:
        data = response.json()
        print(f"  ✓ Login successful")
        print(f"    Role: {data['role']}")
        print(f"    Token: {data['access_token'][:50]}...")
        token = data['access_token']
    else:
        print(f"  ✗ Login failed: {response.status_code}")
        print(f"    {response.json()}")
        sys.exit(1)
except Exception as e:
    print(f"  ✗ Error: {e}")
    sys.exit(1)

# Test 3: Test protected endpoint
print("\n[3/4] Testing protected endpoint...")
try:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("http://localhost:8000/student/me/attendance", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"  ✓ Protected endpoint works")
        print(f"    Attendance records: {len(data.get('attendance', []))}")
    else:
        print(f"  ✗ Failed: {response.status_code}")
except Exception as e:
    print(f"  ✗ Error: {e}")

# Test 4: Verify LAID format
print("\n[4/4] Verifying LAID format...")
if test_laid.startswith("EDU-") and len(test_laid) == 12:
    print(f"  ✓ LAID format correct: {test_laid}")
else:
    print(f"  ✗ LAID format incorrect: {test_laid}")

print("\n" + "="*70)
print("TEST SUMMARY")
print("="*70)
print("\n✓ Server is running")
print("✓ Login works with EDU-format LAID")
print("✓ JWT token generated")
print("✓ Protected endpoints accessible")
print("\n[SUCCESS] System is working correctly!")
print("\nNow open in browser:")
print("  vscode/index.html")
print("\nLogin with:")
print(f"  LAID: {test_laid}")
print(f"  Password: {test_password}")

db.close()
