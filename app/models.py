from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

# try sqlmodel

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(128), index=False)
