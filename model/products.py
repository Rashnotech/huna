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

    def to_dict(self):
        """Converts the Product instance to a dictionary"""
        product_dict = super().to_dict()
        product_dict.update({
            'description': self.description.to_dict() if self.description else None,
            'specification': self.specification.to_dict() if self.specification else None
        })
        return product_dict

