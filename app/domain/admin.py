from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.domain.mixins import UUIDMixin


class Admin(UUIDMixin, Base):
    __tablename__ = "admins"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    user = relationship("User")