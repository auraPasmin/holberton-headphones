""" base_model The mold(idea) class is the parent class."""
import uuid
from datetime import datetime


class BaseModel:
    """class initialization"""
    def __init__(self, *args, **kwargs):
        """ initialization"""

    def __str__(self):
        """should print, and str() should return"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())

    def save(self):
        """comentario"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ comentario"""
    
