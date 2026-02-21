from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.domain.mixins import UUIDMixin, TimestampMixin


class ComplianceLog(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "compliance_logs"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    message = Column(String, nullable=False)
    resolved = Column(Boolean, default=False)

    user = relationship("User")