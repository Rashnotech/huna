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

    method = Column('type', Enum('default', 'installment'), nullable=False)
    order_id = Column(String(100), ForeignKey('orders.id'), nullable=False)
    amount = Column(Float, nullable=False)
    initial = Column(Float, nullable=True)
    balance = Column(Float, nullable=True)
    total_installment = Column(Float, nullable=True)
    duration = Column(Integer, nullable=True)
    order = relationship("Order", backref="payments")

    def __init__(self, **kwargs) -> None:
        """initialization method"""
        super().__init__(**kwargs)
        if self.method == 'installment':
            self.calculate_installments()

    def calculate_installments(self):
        """calculate and set installment details base on the amount
            and rules.
        """
        if self.amount <= 20000:
            raise ValueError("Installment paymemnt is only available for amount above 20,000")
        self.initial = self.amount * 0.1
        self.balance = self.amount - self.initial

        self.total_installment = (self.balance // 10000) + 1
        self.duration = min(30, self.total_installment * 7)

        if self.amount > 500000:
            self.duration = 60

    def validate_amount(cls, v):
        """validate amount"""
        if v <= 0:
            raise ValueError("Amount must be positive""")
        return v

    def validate_method(cls, v):
        if v not in ['default', 'installment']:
            raise ValueError("Invalid payment method")
        return v

    def make_payment(self, amount: float):
        """Handle an installment payment."""
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
        if self.balance <= 0:
            raise ValueError("All installments have been paid")

        if amount > self.balance:
            raise ValueError("Payment amount exceeds remaining balance")

        self.balance -= amount
        self.updated_at = datetime.utcnow()
