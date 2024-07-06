#!/usr/bin/python3
"""a module for product categories"""
from models.base import Base, BaseModel
from sqlalchemy import Column, String


class Category(Base, BaseModel):
    """a category class"""

    __tablename__ = 'categories'

    name = Column(String(100), unique=True, nullable=False)
    link = Column(String(150), nullable=True)

    def __init__(self, **kwargs):
        """initialization"""
        super().__init__(**kwargs)
