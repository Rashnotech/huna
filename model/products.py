#!/usr/bin/env python3
"""a module that handles products modal"""
from model.base import Base, BaseModel




class Product(BaseModel, Base):
    """This class represents a product entity with its attributes and methods."""

    def __init__(self, **kwargs):
        """initialization"""
        super.__init__(**kwargs)
