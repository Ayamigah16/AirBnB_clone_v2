#!/usr/bin/python3
"""Base model module"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import models
import uuid

Base = declarative_base()


class BaseModel:
    """Base model class"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Class constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for k, v in kwargs.items():
                if k not in ["id", "created_at", "updated_at"]:
                    setattr(self, k, v)

    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the current instance from storage"""
        models.storage.delete(self)

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        result = dict(self.__dict__)
        result.pop("_sa_instance_state", None)
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
