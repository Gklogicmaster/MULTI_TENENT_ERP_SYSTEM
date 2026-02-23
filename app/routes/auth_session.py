from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
import uuid

from app.database import get_db
from app.models.students import Student
from app.models.teacher_global import TeacherGlobal
from app.models.admin_global import AdminGlobal

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/auth", tags=["Authentication"])

def generate_laid():
    return f"EDU-{str(uuid.uuid4())[:8]}"

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
def login(laid: str, password: str, db: Session = Depends(get_db)):
    user = None
    role = None
    institution_id = None

    # Try student
    user = db.query(Student).filter(Student.laid == laid).first()
    if user:
        role = "student"
        institution_id = user.institution_id
    
    # Try teacher
    if not user:
        user = db.query(TeacherGlobal).filter(TeacherGlobal.laid == laid).first()
        if user:
            role = "teacher"
            institution_id = getattr(user, 'institution_id', 101)
    
    # Try admin
    if not user:
        user = db.query(AdminGlobal).filter(AdminGlobal.laid == laid).first()
        if user:
            role = "admin"
            institution_id = getattr(user, 'institution_id', 101)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid LAID or password")

    # Verify password
    if getattr(user, "password", None) != password:
        raise HTTPException(status_code=401, detail="Invalid LAID or password")

    # Create JWT token
    token = create_access_token(
        data={
            "sub": laid,
            "role": role,
            "institution_id": institution_id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": role,
        "laid": laid
    }

@router.post("/register")
def register(email: str, password: str, role: str, institution_id: int, db: Session = Depends(get_db)):
    laid = generate_laid()
    # Store plain password for now (same as existing users)
    
    if role == "student":
        new_user = Student(
            laid=laid,
            institution_id=institution_id,
            name=email.split('@')[0],
            branch="General",
            mobile="0000000000",
            email=email,
            gender="Other",
            password=password
        )
    elif role == "teacher":
        new_user = TeacherGlobal(
            laid=laid,
            name=email.split('@')[0],
            email=email,
            password=password
        )
    elif role == "admin":
        new_user = AdminGlobal(
            laid=laid,
            name=email.split('@')[0],
            email=email,
            password=password
        )
    else:
        raise HTTPException(status_code=400, detail="Invalid role")
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"laid": laid, "message": "User registered successfully"}

@router.post("/logout")
def logout():
    return {"message": "Logged out"}