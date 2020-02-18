#!/usr/bin/python3
# Authors:
# test/test_base_model.py.py

"""
    All the test for the base_model are implemented here.
"""
from io import StringIO
import sys
import datetime
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
        Testing in the base class model.
    """

    def setUp(self):
        """
            Initializing instance.
        """
        self.base_model = BaseModel()
        self.base_model.name = "huguito"

    def TearDown(self):
        """
            Removing the instance.
        """
        del self.base_model
     
     def test_docstring(self):
        """the test that confirms if everyone has docstring"""
        self.assertIsNotNone(models.base_model.__doc__,"Module does not has docstring")  # Modules
        self.assertIsNotNone(BaseModel.__doc__, "Clase does not has docstring")  # Classes


if __name__ == '__main__':
    unittest.main()