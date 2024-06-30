#!/usr/bin/env python3
"""a module that handles products modal"""
from model.base import Base, BaseModel
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """
        This class represents a product entity with its
        attributes and methods.
    """
    __tablename__ = 'products'

    name = Column(String(150), nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Integer, nullable=True)
    img_url = Column(String(200), nullable=False)
    link = Column(String(200), nullable=False)
    description = relationship('Description', uselist=False,
                               back_populates='product',
                               cascade='all, delete-orphan')
    specification = relationship('Specification', uselist=False,
                                 back_populates='product',
                                 cascade='all, delete-orphan')

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
