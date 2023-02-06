from models import User
from schemas.users import UserBase
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from main import app

@app.get("/")
async def home():
    return {"message":"Folzeck Group"}

@app.get("/users/{user_id}")
async def list_user_by_index(index:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.user.id==index).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID{index}:Does not exist"
        )
    else:
        return db.query(User).filter(User.user_id==index).first()

@app.post("/add-user")
async def add_user(user:UserBase, db:Session=Depends(get_db))->UserBase:
    user_model = User()
    user_model.name = user.name
    user_model.lastname = user.lastname
    user_model.age = user.age
    user_model.genre = user.genre

    db.add(user_model)
    db.commit()
    return user