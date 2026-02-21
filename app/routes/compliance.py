from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.domain.compliance import ComplianceLog

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/alerts/{user_id}")
def get_alerts(user_id: str, db: Session = Depends(get_db)):
    alerts = db.query(ComplianceLog).filter(
        ComplianceLog.user_id == user_id,
        ComplianceLog.resolved == False
    ).all()

    return alerts