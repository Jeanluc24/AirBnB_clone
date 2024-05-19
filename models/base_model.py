#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from datetime import datetime
import uuid


class BaseModel:
    """Repsents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """initializes a base model
        Args:
            *args: unused
            **kwargs: k/v pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        isof = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k.endswith('at') and isinstance(v, str):
                    self.__dict__[k] = datetime.strptime(v, isof)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """updates update_at attribute with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        myi_dict = self.__dict__.copy()
        myi_dict["created_at"] = self.created_at.isoformat()
        myi_dict["updated_at"] = self.updated_at.isoformat()
        myi_dict['__class__'] = self.__class__.__name__
        return (myi_dict)

    def __str__(self):
        """prints Base_model instances"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
