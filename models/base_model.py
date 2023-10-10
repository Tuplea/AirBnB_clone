#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
from json import dumps, loads
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """This class defines all common attributes/methods for other classes"""


    __ids_set = {}

    def __init__(self):
        """Initialises the classe with the following attribs :
            id: string - assigned with an uuid4() when an instance is created:
                the goal is to have unique id for each BaseModel
            created_at: datetime - assigned the current datetime 
                when an instance is created
            updated_at: datetime - assigned the current datetime 
                when an instance is created and it will be updated 
                every time the object changes"""
        self.id = uuid4().__str__
        self.created_at =  datetime.now()
        self.updated_at = datetime.now()

    def create_id(self):
        """DEPRECATED -- generates a safer random id"""
        MAX_ITIRATION = 100     #the maximum iteration number for obtaining a valid unique id
        for i in range(MAX_ITIRATION):
            id = uuid4().__str__
            if id not in self.__ids_set:
                self.__ids_set.append(id)
                return (id)
            i += 1
        return (None)           #Failed to obain the id
    
    def __str__(self):
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()

        return (dict)
