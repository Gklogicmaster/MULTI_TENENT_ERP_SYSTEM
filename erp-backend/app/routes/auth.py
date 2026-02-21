from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, LoginRequest
from app.schemas.token import Token
from app.services.auth_service import register_user, authenticate_user
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, request.laid, request.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid LAID or Password")

    token = create_access_token(
        data={
            "sub": str(user.id),
            "role": user.role.name,   # if using relationship
            "laid": user.laid
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }