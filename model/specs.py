#!/usr/bin/env python3
"""a module that models the product specification"""
from model.base import Base, BaseModel


class Specs(BaseModel, Base):
    """a specification class for product"""

    def __init__(self, product, **kwargs):
        super.__init__(**kwargs)
        product_id = product.id