from sqlalchemy import Column, String
from app.db.base import Base
from app.domain.mixins import UUIDMixin


class Role(UUIDMixin, Base):
    __tablename__ = "roles"

    name = Column(String, unique=True, nullable=False)