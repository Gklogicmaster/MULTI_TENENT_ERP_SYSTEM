from sqlalchemy import Column, String
from app.db.base import Base
from app.domain.mixins import UUIDMixin, TimestampMixin


class Institution(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "institutions"

    name = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)