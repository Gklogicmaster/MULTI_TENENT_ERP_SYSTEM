from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from pydantic import BaseModel
from typing import List
import uuid

from app.db.database import SessionLocal
from app.domain.compliance import ComplianceLog

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Response schema
class ComplianceResponse(BaseModel):
    id: uuid.UUID
    message: str
    resolved: bool

    class Config:
        from_attributes = True


@router.get("/alerts/{user_id}", response_model=List[ComplianceResponse])
def get_alerts(user_id: str, db: Session = Depends(get_db)):

    try:
        user_uuid = uuid.UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID")

    alerts = db.query(ComplianceLog).filter(
        ComplianceLog.user_id == user_uuid,
        ComplianceLog.resolved == False
    ).all()

    return alerts