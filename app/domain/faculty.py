from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.domain.mixins import UUIDMixin


class Faculty(UUIDMixin, Base):
    __tablename__ = "faculty"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    qualification = Column(String)
    age = Column(Integer)
    phone = Column(String)
    salary = Column(Float)
    handling_courses = Column(String)

    user = relationship("User")