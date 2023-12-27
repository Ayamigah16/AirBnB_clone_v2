#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class"""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
    places = relationship("Place", backref="city", cascade="all, delete-orphan")
