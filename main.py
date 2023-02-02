from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db()
    try: 
        db = SessionLocal()
        yield db
    finally:
        db.close()

class User(BaseModel):
    name: str
    lastname:str
    user_id: Optional[str] = uuid4().hex
    age: int
    genre:Literal["Male", "Female"]
    
