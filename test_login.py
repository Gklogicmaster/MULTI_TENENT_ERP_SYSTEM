"""Test login API endpoint"""
import requests

# Test login
url = "http://localhost:8000/auth/login"
params = {
    "role": "student",
    "laid": "S101-ABC123",
    "password": "student123",
    "institution_id": 101
}

print("Testing login API...")
print(f"URL: {url}")
print(f"Params: {params}")

try:
    response = requests.post(url, params=params)
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        print("\n✓ Login successful!")
    else:
        print("\n✗ Login failed!")
        
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nMake sure the server is running:")
    print("  python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
