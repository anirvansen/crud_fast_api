from datetime import timedelta
import os
from typing import List

from fastapi import Depends, FastAPI, HTTPException,status,Form
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm




from . import models, schemas,crud,auth
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

#For JWT token
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



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


@app.post("/register")
def register_user(username: str = Form(...), password: str = Form(...),db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db = db,username = username)

    if db_user:
        raise HTTPException(status_code=400,detail="User already registerd")

    user = schemas.User(username= username,password = password)
    return crud.create_user(db = db,user = user)


@app.post("/token",status_code=status.HTTP_200_OK,response_model=schemas.Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
    username = form_data.username
    password = form_data.password
    db_user = crud.get_user_by_username(db = db,username = username)
    if db_user:
        if crud.verify_password(password,db_user.password):
            #Now we can genearate the token
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = auth.create_access_token(
                data={"sub": db_user.username}, expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "bearer"}

        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password")

    raise HTTPException(status_code=400,detail="User not found!")


@app.post("/product")
def add_product(product : schemas.Product,db = Depends(get_db),authenticated : bool = Depends(auth.isAutheticated)):
    product_item = crud.add_product(db=db,product = product)
    return  {"msg" : "Product is successfully added!"}

@app.get("/product",response_model=List[schemas.ProductResponse])
def get_products(db= Depends(get_db)):
    return crud.get_products(db=db)

@app.delete("/product/<id>")
def delete_product(id : int,db = Depends(get_db),authenticated : bool = Depends(auth.isAutheticated)):
    product = crud.get_product_by_id(db = db , id = id)
    if product:
        message = crud.delete_product(db = db , product = product)
        return {"msg" : message}

    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Product id = {id} not found in database")

@app.put("/product/<id>")
def update_product(id: int , new_product : schemas.Product,db = Depends(get_db),authenticated : bool = Depends(auth.isAutheticated)):
    product = crud.get_product_by_id(db = db , id = id)
    if product:
        message = crud.update_product(db = db , existing_product = product , new_product = new_product)
        return {"msg" : message}

    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Product id = {id} not found in database")

    