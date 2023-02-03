from pydantic import BaseModel
from typing import Literal
class UserBase(BaseModel):
    name: str
    lastname:str
    age: int
    genre:Literal["Male", "Female"]