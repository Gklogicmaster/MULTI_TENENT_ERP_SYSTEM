from sqlalchemy import Column, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.domain.mixins import UUIDMixin


class Student(UUIDMixin, Base):
    __tablename__ = "students"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    attendance = Column(Float)
    fees = Column(Float)
    course = Column(String)
    cgpa = Column(Float)
    marks = Column(Float)
    branch = Column(String)
    phone = Column(String)
    gender = Column(String)

    user = relationship("User")