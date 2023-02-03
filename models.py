from sqlalchemy import Column, Integer, String 
from database import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lastname =  Column(String)
    age = Column(Integer)
    genre = Column(String)