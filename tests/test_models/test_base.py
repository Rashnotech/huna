#!/usr/bin/python3
"""a module that test base class"""
import unittest
from model.base import BaseModel


class TestBaseModel(unittest.TestCase):
    """a class that test the implementation of the base class"""
    def setUp(self):
        """Initialization method"""
        self.base = BaseModel()

    def test_attributes(self):
        """a method that test class attributes"""
        self.assertTrue(type(self.base.id), str)


if __name__ == '__main__':
    unittest.main()
