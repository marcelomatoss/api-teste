import models
from database import engine, SessionLocal
import db
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import User
from schemas.users import UserBase
app = FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    try: 
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/list-user")
async def list_user(user: UserBase, db: Session = Depends(db.get_db)):
    return db.query(User).all()
