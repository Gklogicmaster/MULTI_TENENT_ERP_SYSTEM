from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.domain.mixins import UUIDMixin, TimestampMixin


class User(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "users"

    laid = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id"))

    role = relationship("Role")
    institution = relationship("Institution")