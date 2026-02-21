from fastapi import FastAPI
from app.database import engine, Base
import app.models
from app.routes import auth

app = FastAPI()

app.include_router(auth.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "ERP Backend Running"}