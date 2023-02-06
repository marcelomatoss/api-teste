from models import User
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
import models
from main import app

models.Base.metadata.create_all(bind=engine)

def get_db():
    try: 
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/list-user")
async def list_user(db:Session=Depends(get_db)):
    return db.query(User).all()