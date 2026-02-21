from app.db.base import Base
from app.db.database import engine
from app.domain import ComplianceLog

# Import models so they register
from app.domain import Institution, Role, User, Student, Faculty, Admin


def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")


if __name__ == "__main__":
    init_db()