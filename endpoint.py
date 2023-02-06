from models import User
from schemas.users import UserBase
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
import db
app = FastAPI()

@app.get("/")
async def home():
    return {"message":"Folzeck Group"}

@app.get("/list-user")
async def list_user(user:UserBase,db:Session=Depends(db.get_db)):
    return db.query(User).all()

@app.get("/users/{user_id}")
async def list_user_by_index(index:int,db:Session=Depends(db.get_db)):
    user=db.query(models.Users).filter(models.Users.user.id==index).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID{index}:Does not exist"
        )
    else:
        return db.query(models.Users).filter(models.Users.user_id==index).first()
