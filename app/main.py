from fastapi import FastAPI
from app.routes.compliance import router as compliance_router
from app.routes.academic import router as academic_router

app = FastAPI(title="ERP Backend")

app.include_router(compliance_router, prefix="/compliance", tags=["Compliance"])
app.include_router(academic_router, prefix="/academic", tags=["Academic"])

@app.get("/")
def root():
    return {"message": "Backend Server Running"}