#!/usr/bin/python3
"""a module for user of the app"""
from model.base import Base, BaseModel
from sqlalchemy import Column, String
from hashlib import md5


class User(Base, BaseModel):
    """a class for class model"""

    __tablename__ = 'users'

    username = Column(String(100), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(150), nullable=False)


    def __init__(self, **kwargs):
        """initialization"""
        super().__init__(**kwargs)

    def set_password(self, password):
        """set password"""
        self.password = md5(password)
