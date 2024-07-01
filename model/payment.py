#!/usr/bin/python3
"""a module that handles payment"""
from model.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Enum
from sqlalchemy.orm import relationship


class Payment(BaseModel, Base):
    """
    A class that handles payment transactions
    """

    __tablename__ = 'payments'

    payment_method = Column('type', Enum('one-off', 'recurring'), nullable=False)
    order_id = Column(String(100), ForeignKey('orders.id'), nullable=False)
    amount = Column(Float, nullable=False)

    def __init__(self, **kwargs) -> None:
        """initialization method"""
        super().__init__(**kwargs)

