#!/usr/bin/env python3
"""a module that models the product specification"""
from model.base import Base, BaseModel
from sqlalchemy import Column, String, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Specification(BaseModel, Base):
    """a specification class for product"""

    __tablename__ = 'specifics'

    title = Column(String(100))
    specification = Column(Text, nullable=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    product = relationship('Product', back_populates='specification',
                           uselist=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
