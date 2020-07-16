from typing import List

from fastapi import Depends, FastAPI, HTTPException,status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from . import models, schemas,crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.post("/register/")
def register_user(user : schemas.User,db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db = db,email = user.email)
    if db_user:
        raise HTTPException(status_code=400,detail="Email already registerd")
    return crud.create_user(db = db,user = user)


@app.post("/login/",status_code=status.HTTP_200_OK)
def login_user(user : schemas.LoginUser,db : Session = Depends(get_db)):
    print(user.email)
    db_user = crud.get_user_by_email(db = db,email = user.email)
    if db_user:
        if crud.verify_password(user.password,db_user.password):
            print("password is verified")
            return {"Message" : "User is verified"}

        else:
            raise HTTPException(status_code=401,detail="Email or password is not matching!")



    raise HTTPException(status_code=400,detail="User not found!")
    