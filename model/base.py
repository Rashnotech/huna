#!/usr/bin/env python3
"""base class for scrapper entity"""
from uuid import uuid4
from sqlalchemy import Column, Integer, DateTime 
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel:
    """A class that represents a base entity with its attributes and methods."""
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)

    def __init__(self, **kwargs) -> None:
        """initialization method"""
        if kwargs:
            for attr, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, attr, datetime.strptime(value,
                                                          '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == '__class__':
                    del key
                else:
                    setattr(self, attr, value)
        else:
            self.id = uuid4()
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
    