#!/usr/bin/env python3
"""a ecommerce description model"""
from model.base import Base, BaseModel


class Description(BaseModel, Base):
    """
    A class that stores product description
    """

    def __init__(self, product, **kwargs) -> None:
        super().__init__(**kwargs)
        product_id = product.id