#!/usr/bin/python3
"""a module for user of the app"""
from model.base import Base, BaseModel
from sqlalchemy import Column, String, Boolean
from hashlib import md5


class User(Base, BaseModel):
    """a class for class model"""

    __tablename__ = 'users'

    username = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    verify = Column(Boolean, nullable=False, default=False)
    password = Column(String(150), nullable=False)


    def __init__(self, **kwargs) -> None:
        """initialization"""
        super().__init__(**kwargs)
        self.password = md5(self.password.encode()).hexdigest()

    def set_password(self, new_password) -> str:
        """set password"""
        self.password = new_password
