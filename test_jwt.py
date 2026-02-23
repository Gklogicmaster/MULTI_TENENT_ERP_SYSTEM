"""Test JWT Authentication"""
from app.routes.auth_session import create_access_token, verify_password
from jose import jwt

print("="*60)
print("JWT AUTHENTICATION TEST")
print("="*60)

# Test 1: Create token
print("\n[1/2] Testing token creation...")
token_data = {
    "sub": "S101-ABC123",
    "role": "student",
    "institution_id": 101
}
token = create_access_token(token_data)
print(f"[OK] Token created: {token[:50]}...")

# Test 2: Decode token
print("\n[2/2] Testing token verification...")
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print(f"[OK] Token decoded successfully")
print(f"     LAID: {payload['sub']}")
print(f"     Role: {payload['role']}")
print(f"     Institution: {payload['institution_id']}")

print("\n" + "="*60)
print("[SUCCESS] JWT Authentication is working!")
print("="*60)
print("\nYou can now:")
print("1. Start server: python -m uvicorn app.main:app --reload")
print("2. Login will return JWT token")
print("3. Token is used for all authenticated requests")
