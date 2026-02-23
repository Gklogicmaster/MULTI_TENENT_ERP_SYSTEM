from sqlalchemy import Column, Integer, String
from app.database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    laid = Column(String, index=True, nullable=False)
    institution_id = Column(Integer, index=True, nullable=False)

    course_code = Column(String, nullable=True)
    status = Column(String, nullable=False, default="Present")
    date = Column(String, nullable=True)