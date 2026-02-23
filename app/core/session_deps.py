from fastapi import Depends, HTTPException, Header
from jose import JWTError, jwt

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    
    token = authorization.replace("Bearer ", "")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_student(payload: dict = Depends(verify_token)):
    if payload.get("role") != "student":
        raise HTTPException(status_code=403, detail="Not a student")
    return {"laid": payload.get("sub"), "institution_id": payload.get("institution_id")}

def get_current_teacher(payload: dict = Depends(verify_token)):
    if payload.get("role") != "teacher":
        raise HTTPException(status_code=403, detail="Not a teacher")
    return {"laid": payload.get("sub"), "institution_id": payload.get("institution_id")}

def get_current_admin(payload: dict = Depends(verify_token)):
    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not an admin")
    return {"laid": payload.get("sub"), "institution_id": payload.get("institution_id")}