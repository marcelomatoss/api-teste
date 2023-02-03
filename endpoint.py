from models import User
from schemas.users import UserBase
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import db
app = FastAPI()

@app.get("/")
async def home():
    return {"message":"Folzeck Group"}

@app.get("/list-user")
async def list_user(user: UserBase, db: Session = Depends(db.get_db)):
    return db.query(User).all()

