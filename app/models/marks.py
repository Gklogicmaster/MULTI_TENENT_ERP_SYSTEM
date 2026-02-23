from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)
    laid = Column(String, index=True, nullable=False)
    institution_id = Column(Integer, index=True, nullable=False)

    course_code = Column(String, nullable=False)
    exam_type = Column(String, nullable=True)
    marks = Column(Float, nullable=False)
    max_marks = Column(Float, nullable=True)