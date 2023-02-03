import models
import schemas.users
import database
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import db
app = FastAPI()

@app.get("/")
async def home():
    return {"message":"Folzeck Group"}

@app.get("/list-user")
async def list_user(user: schemas.users.UserBase, db: Session = Depends(db.get_db)):
    return db.query(models.User).all()

