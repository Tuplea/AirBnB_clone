##!/usr/bin/python3
"""FileStorage class that handles file serialization/deserialisation"""
import json
from models.base_model import BaseModel


class FileStorage():
    """serialisation class"""

    __file_path = "memory.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        #mine
        self.__objects[str(obj.__class__.__name__) + "." + str(obj.id)] = obj

    def save_original(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objects_dic_rep = {}
        for obj in FileStorage.__objects.keys():
            objects_dic_rep[obj] = FileStorage.__objects[obj].to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dic_rep, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                objs_dict = json.load(file)
                for obj in objs_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
