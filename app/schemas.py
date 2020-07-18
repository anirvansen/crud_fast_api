from datetime import date
from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    username : str
    password : str

    class Config:
        orm_mode = True

class LoginUser(BaseModel):
    email : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str

class Product(BaseModel):
    name : str
    description : str
    price : float

    class Config:
        orm_mode = True



class ProductResponse(BaseModel):
    id : int
    name : str
    description : str
    price : float
    created_on : str
    updated_on : str

    class Config:
        orm_mode = True