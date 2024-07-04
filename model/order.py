#!/usr/bin/python3
"""a module that handle order"""
from model.base import Base, BaseModel
from sqlalchemy import Column, JSON, String, ForeignKey, Integer, Float, Enum
from enum import Enum as PythonEnum
from sqlalchemy.orm import relationship

class OrderEnum(PythonEnum):
    """enum for order status"""
    default = 'default'
    pending = 'pending'
    processing = 'processing'
    shipped = 'shipped'
    in_transit = 'in-transit'
    delivered = 'delivered'
    cancelled = 'cancelled'
    returned = 'returned'
    refunded = 'refunded'
    failed = 'failed'
    complete = 'completed'


class Order(Base, BaseModel):
    """a model for ordered products"""

    __tablename__ = 'orders'

    order_id = Column(String(100), ForeignKey('order_items.id'),
                      nullable=False)
    status = Column(Enum(OrderEnum, length=20), default=OrderEnum.default)
    user_id = Column(String(100), ForeignKey('users.id'), nullable=False)

    def __init__(self, **kwargs):
        """Initialization"""
        super().__init__(**kwargs)



class Item(Base, BaseModel):
    """a model for ordered items"""

    __tablename__ = 'order_items'

    checkout = Column(JSON)
    user_id = Column(String(100), ForeignKey('users.id'), nullable=False)

    def __init__(self, **kwargs):
        """initialization"""
        super().__init__(**kwargs)
