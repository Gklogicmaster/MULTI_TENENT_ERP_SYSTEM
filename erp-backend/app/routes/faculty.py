from fastapi import APIRouter, Depends
from app.core.security import require_role

router = APIRouter(prefix="/faculty", tags=["Faculty"])

@router.get("/dashboard")
def faculty_dashboard(user = Depends(require_role("faculty"))):
    return {
        "message": "Welcome Faculty",
        "user": user
    }