#!/usr/bin/env python3
"""a ecommerce description model"""
from model.base import Base, BaseModel
from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Description(BaseModel, Base):
    """
    A class that stores product description
    """

    __tablename__ = 'description'

    title = Column(String(100), nullable=False)
    features = Column(Text)
    product_id = Column(String(50), ForeignKey('products.id'), nullable=False)
    product = relationship('Product', back_populates='description',
                           uselist=False)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
