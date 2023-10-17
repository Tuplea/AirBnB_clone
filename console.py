#!/usr/bin/python3
"""Cmd class : the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""

    prompt = "(hbnb) "
    allowed_classes = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """Quits the command prompt"""
        return True

    def do_EOF(self, line):
        """Quits the command prompt"""
        return True

    def do_create(self, line):
        """creates a new instance of the class called
    Usage : create <class name>"""
        if len(line.split()) > 1:
            print("Usage : create <class name>")
        elif len(line) < 1:
            print("** class name missing **")
        else:
            try:
                my_model = eval(line + "()")
                print(my_model.id)
                my_model.save()
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Shows more info about an instance
    Usage : show <class name> <id>"""
        storage = FileStorage.all(FileStorage)
        if len(line.split()) > 2:
            print("Usage : show <class name> <id>")
        elif len(line) < 1:
            print("** class name missing **")
        elif len(line.split(" ")) < 2:
            print("** instance id missing **")
        else:
            try:
                class_name = line.split(" ")[0]
                id = line.split(" ")[1]
                print(str(storage[class_name + "." + id]))
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance by id
    Usage : delete <class name> <id>"""
        if 0:
            # len(line.split()) > 2:
            # print("Usage : show <class name> <id>")
            pass
        elif len(line) < 1:
            print("** class name missing **")
        elif len(line.split(" ")) < 2:
            print("** instance id missing **")
        elif line.split(" ")[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            class_name = line.split(" ")[0]
            id = line.split(" ")[1]
            try:
                del FileStorage.all(FileStorage)[class_name + "." + id]
                FileStorage.save(FileStorage)
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """prints all the str repr of stored model
    Usage 1 : all
And can also specify the <class name> to print all instances of that class
    Usage 2 : all <class name>"""
        if len(line.split()) > 2:
            print("Usage 1 : all <class name>\nUsage 2 : all")
        elif len(line) < 1:
            # no args print everything stored
            objs_str_list = []
            for key in FileStorage.all(FileStorage).keys():
                objs_str_list.append(str(FileStorage.all(FileStorage)[key]))
            print(objs_str_list)
        # elif line.split(" ")[0] not in FileStorage.all(FileStorage):
            # print("** class doesn't exist **")
        elif len(line.split(" ")) < 2:
            # ClassName arg is given
            if len(FileStorage.all(FileStorage).keys()):
                for key in FileStorage.all(FileStorage).keys():
                    if len(FileStorage.all(FileStorage).keys()) == 0:
                        print("** class doesn't exist **")
                    if key.split('.')[0] == line.split(' ')[0]:
                        print(str(FileStorage.all(FileStorage)[key]))
                    else:
                        print("** class doesn't exist **")
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by
adding or updating attribute
    Usage: update <class name> <id> <attribute name> \"<attribute value>\""""
        storage = FileStorage.all(FileStorage)
        if len(line.split()) < 4:
            if len(line.split()) == 0:
                print("** class name missing **")
            elif len(line.split()) == 1:
                print("** instance id missing **")
            elif len(line.split()) == 2:
                print("** attribute name missing **")
            elif len(line.split()) == 3:
                print("** value missing **")
        elif line.split(" ")[0] not in FileStorage.all(FileStorage):
            print("** class doesn't exist **")
        else:
            try:
                for key in storage.keys():
                    if (key.split('.')[0] == line.split(' ')[0]):
                        # class name exists
                        pass
                    else:
                        print("** class doesn't exist **")
                class_name = line.split(" ")[0]
                id = line.split(" ")[1]
                attrib_name = line.split(" ")[2]
                attrib_value = eval(line.split(" ")[3])
                obj = storage[class_name + "." + id]
                obj.__dict__[attrib_name] = attrib_value
                if attrib_name == "id":
                    # changing the id is storage file
                    old_key = class_name + "." + id
                    new_key = class_name + "." + attrib_value
                    storage[new_key] = storage[old_key]
                    del storage[old_key]
                obj.save()
            except KeyError:
                print("** no instance found **")

    def get_objects(self, instance=''):
        """Gets the elements stored in memory"""
        objects = FileStorage.all(FileStorage)

        if instance:
            keys = objects.keys()
            return [str(val) for key, val in objects.items()
                    if key.startswith(instance)]

        return [str(val) for key, val in objects.items()]

    def default(self, line):
        """defaul value handler"""
        if '.' in line:
            splitted_line = re.split(r'\.|\(|\)', line)
            class_name = splitted_line[0]
            method_name = splitted_line[1]

            if class_name in self.allowed_classes:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    class_id = splitted_line[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted_line[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)
                else:
                    super().default(line)

            else:
                print("** class doesn't exist **")

    def defaulti_old(self, line):
        """handles <class name>.<function> calls"""

        if self.line_to_cmd(line):
            # change print to eval
            try:
                eval("self.do_" + self.line_to_cmd(line)[1] + "(" + "\""
                     + self.line_to_cmd(line)[0] + " "
                     + self.line_to_cmd(line)[2] + "\"" + ")")
            except AttributeError:
                super().default(line)
            except NameError:
                super().default(line)
            except SyntaxError:
                super().default(line)
        else:
            super().default(line)

    @staticmethod
    def line_to_cmd(line):
        """processes the ClassName.Command(Arg) format calls
returns False if something went south"""
        # ex : User.create()     User.show("aabbvv")
        if "." in line and "(" in line and ")" in line:
            try:
                cls_name = line.split(".")[0]
                funct = line.split(".")[1].split("(")[0]
                arg = line.split(".")[1].split("(")[1].split(")")[0]
                return [cls_name, funct, arg]
            except IndexError:
                return False
        else:
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
