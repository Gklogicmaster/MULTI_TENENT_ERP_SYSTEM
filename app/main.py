from fastapi import FastAPI
from app.routes.compliance import router as compliance_router

app = FastAPI()

# Include routers AFTER app is created
app.include_router(compliance_router)


@app.get("/")
def root():
    return {"message": "Backend Server Running"}