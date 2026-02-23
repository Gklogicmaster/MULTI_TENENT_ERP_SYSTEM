from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)
    laid = Column(String, index=True, nullable=False)
    institution_id = Column(Integer, index=True, nullable=False)

    total_amount = Column(Float, nullable=False)
    paid_amount = Column(Float, default=0)
    due_amount = Column(Float, default=0)
    semester = Column(String, nullable=True)