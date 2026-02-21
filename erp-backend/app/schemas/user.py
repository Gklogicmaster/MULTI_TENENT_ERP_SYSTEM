from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    role: str
    institution_id: int

class LoginRequest(BaseModel):
    laid: str
    password: str