#!/usr/bin/python3
"""State module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    def to_dict(self):
        """Return a dictionary representation of the object."""
        obj_dict = super().to_dict()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['name'] = self.name
        # Add any other state-specific attributes
        return obj_dict
