#!/usr/bin/env python3
"""base class for scrapper entity"""
from uuid import uuid4
from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A class that represents a base entity with its attributes
        and methods.
    """
    id = Column(String(50), unique=True, default=lambda: str(uuid4()),
                primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc),
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.now(timezone.utc),
                        nullable=False)

    def __init__(self, **kwargs) -> None:
        """initialization method"""
        if kwargs:
            for attr, value in kwargs.items():
                if attr in ['created_at', 'updated_at']:
                    setattr(self, attr,
                            datetime.strptime(value,
                                              '%Y-%m-%dT%H:%M:%S.%f'))
                elif attr == '__class__':
                    del attr
                else:
                    setattr(self, attr, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)

    def __str__(self) -> str:
        #returns a string representation
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def to_dict(self) -> dict:
        """
            returns a dictionary containing all key/values of dict of
            class instance
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def save(self) -> None:
        from model import storage
        """updates the public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now(timezone.utc)
        storage.new(self)
        storage.save()

    def delete(self) -> None:
        from model import storage
        """deletes the current instance from the storage"""
        storage.delete(self)
