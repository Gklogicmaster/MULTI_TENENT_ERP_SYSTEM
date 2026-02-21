import uuid
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.role import Role
from app.core.security import hash_password, verify_password

def generate_laid():
    return f"EDU-{str(uuid.uuid4())[:8]}"

def register_user(db: Session, user_data):
    role = db.query(Role).filter(Role.name == user_data.role).first()
    if not role:
        raise ValueError("Role not found")

    new_user = User(
        laid=generate_laid(),
        email=user_data.email,
        password=hash_password(user_data.password),
        role_id=role.id,
        institution_id=user_data.institution_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, laid: str, password: str):
    user = db.query(User).filter(User.laid == laid).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user