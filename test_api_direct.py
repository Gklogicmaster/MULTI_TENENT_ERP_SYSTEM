"""Test login API directly"""
import requests
import sys

print("Testing login API...")
print("-" * 50)

# Test if server is running
try:
    response = requests.get("http://localhost:8000/", timeout=2)
    print("[OK] Server is running")
except:
    print("[ERROR] Server is NOT running!")
    print("\nStart server first:")
    print("  python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    sys.exit(1)

# Test login
url = "http://localhost:8000/auth/login"
params = {
    "role": "student",
    "laid": "S101-ABC123",
    "password": "student123",
    "institution_id": 101
}

print(f"\nTesting: {url}")
print(f"Params: {params}")

try:
    response = requests.post(url, params=params)
    print(f"\nStatus: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        print("\n[SUCCESS] Login works!")
    else:
        print("\n[ERROR] Login failed!")
        print("Check backend logs for details")
except Exception as e:
    print(f"\n[ERROR] {e}")
