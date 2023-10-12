#!/usr/bin/python3
"""FileStorage class that handles file serialization/deserialisation"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """serialisation class"""

    __file_path = "memory.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[str(obj.__class__.__name__) + "." + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objects_dic_rep = {}
        for obj in FileStorage.__objects.keys():
            objects_dic_rep[obj] = FileStorage.__objects[obj].to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dic_rep, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects if it exists"""
        try:
            with open(FileStorage.__file_path) as file:
                objs_dict = json.load(file)
                for obj in objs_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
