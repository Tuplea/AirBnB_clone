#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
from json import dumps, loads
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kargs):
        """Initialises the classe with the following attribs :
            id: string - assigned with an uuid4() when an instance is created:
                the goal is to have unique id for each BaseModel
            created_at: datetime - assigned the current datetime
                when an instance is created
            updated_at: datetime - assigned the current datetime
                when an instance is created and it will be updated
                every time the object changes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

#       creating an obj from a dict repr passerd as kargs
#       time_format is used by strptime
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kargs) != 0:
            for key, value in kargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """str representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.FileStorage.save(models.FileStorage)

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dictt = self.__dict__.copy()
        dictt["__class__"] = self.__class__.__name__
        dictt["created_at"] = self.created_at.isoformat()
        dictt["updated_at"] = self.updated_at.isoformat()

        return dictt
