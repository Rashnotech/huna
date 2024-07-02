#!/usr/bin/python3
"""a module that handle order"""
from model.base import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Enum


class Order(Base, BaseModel):
    """a model for ordered products"""

    __tablename__ = 'orders'

    status = Column('status', Enum('default', 'pending', 'completed'),
                    nullable=False)
    user_id = Column(String(100), ForeignKey('users.id'), nullable=False)

    def __init__(self, **kwargs):
        """Initialization"""
        super().__init__(**kwargs)



class Item(Base, BaseModel):
    """a model for ordered items"""

    __tablename__ = 'order_items'

    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    order_id = Column(String(100), ForeignKey('orders.id'), nullable=False)
    product_id = Column(String(100), ForeignKey('products.id'), nullable=False)

    def __init__(self, **kwargs):
        """initialization"""
        super().__init__(**kwargs)
