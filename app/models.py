from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from .database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(30))
    email = Column(String(30))
    password = Column(String(30))

    def __repr__(self):
        return f"{self.__class__.__name__}(fullname = {self.fullname},email = {self.email})"