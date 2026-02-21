from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User( Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    laid = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    institution_id = Column(Integer, ForeignKey("institutions.id"), nullable=False)

    role = relationship("Role", back_populates="users")
    institution = relationship("Institution", back_populates="users")