from sqlalchemy.orm import Session
import datetime
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.User):
    hashed_password = get_password_hash(user.password )
    db_user = models.User(fullname=user.fullname, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(db_user)
    print(type(db_user))
    return db_user


def add_product(db : Session, product : schemas.Product):
    name = product.name
    description = product.description
    price  = product.price
    created_on = datetime.datetime.utcnow()
    updated_on = "" #None when creating the product for the first time

    product_item = models.Product(name=name,
                                  description=description,
                                  price=price,
                                  created_on=created_on,
                                  updated_on=updated_on)
    db.add(product_item)
    db.commit()
    db.refresh(product_item)
    return product_item


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product_by_id(db: Session, id : int):
    return db.query(models.Product).filter(models.Product.id == id).first()


def delete_product(db : Session,product : schemas.Product):
    db.delete(product)
    db.commit()
    return "Successfully deleted"


def update_product(db : Session, existing_product : models.Product, new_product ):
    existing_product.name = new_product.name
    existing_product.price = new_product.price
    existing_product.description = new_product.description
    existing_product.updated_on = datetime.datetime.utcnow()
    db.commit()
    db.refresh(existing_product)
    return  "Successfully updated!"



