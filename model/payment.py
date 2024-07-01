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

    payment_type = Column('type', Enum('one-off', 'recurring'), nullable=False)
    order_items = Column(String(100), unique=True, ForeignKey())
    amount = Column(Float, nullable=False)
    product_id = Column(String(100), unique=True, ForeignKey(),
                        nullable=False)

    def __init__(self, **kwargs) -> None:
        """initialization method"""
        super().__init__(**kwargs)

