from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    fullname : str
    email : str
    password : str

    class Config:
        orm_mode = True

class LoginUser(BaseModel):
    email : str
    password : str