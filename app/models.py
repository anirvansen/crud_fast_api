from sqlalchemy import Column, Integer, String,Float
from sqlalchemy.types import Date
from .database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30))
    password = Column(String(30))

    def __repr__(self):
        return f"{self.__class__.__name__}(fullname = {self.username})"


class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    description = Column(String(40))
    price = Column(Float)
    created_on = Column(String(30))
    updated_on = Column(String(30))

    def __repr__(self):
        return f"{self.__class__.__name__}(Product_name = {self.name})"