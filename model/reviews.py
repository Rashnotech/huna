#!/usr/bin/python3
"""a module for product reviews"""
from model.base import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String, Integer, Text


class Review(Base, BaseModel):
    """
    A model for product review
    """

    __tablename__ = 'reviews'

    comment = Column(Text, nullabe=False)
    rating = Column(Integer, nullable=False)
    user_id = Column(String(100), ForeignKey('users.id'), nullable=False)
    product_id = Column(String(100), ForeignKey('products.id'), nullable=False)

    def __init__(self, **Kwargs):
        """class initialization"""
        super().__init__(**kwargs)
