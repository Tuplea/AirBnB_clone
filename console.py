#!/usr/bin/python3
"""Cmd class : the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quits the command prompt"""
        return True
    
    def do_EOF(self, line):
        """Quits the command prompt"""
        return True
    
    def do_create(self, line):
        """creates a new instance of the class called
        Usage : create <class name>"""
        if len(line.split( )) > 1:
            print("Usage : create <class name>")
        elif len(line) < 1:
            print("** class name missing **")
        else:
            try :
                my_model = eval(line + "()")
                print(my_model.id)
                my_model.save()
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Shows more info about an instance
        Usage : show <class name> <id>"""
        if len(line.split( )) > 2:
            print("Usage : show <class name> <id>")
        elif len(line) < 1:
            print("** class name missing **")
        elif len(line.split(" ")) < 2:
            print("** instance id missing **")
        else:
            try:
                class_name = line.split(" ")[0]
                id = line.split(" ")[1]
                print(str(FileStorage.all(FileStorage)[class_name + "." + id]))
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance by id
        Usage : delete <class name> <id>"""
        if len(line.split( )) > 2:
            print("Usage : show <class name> <id>")
        elif len(line) < 1:
            print("** class name missing **")
        elif len(line.split(" ")) < 2:
            print("** instance id missing **")
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
        And can also specify the ClassName to print all instances
        of that class
        Usage 2 : all <class name>"""
        if len(line.split( )) > 2:
            print("Usage 1 : all <class name>\nUsage 2 : all")
        elif len(line) < 1:
            #no args print everything stored
            objs_str_list = []
            for key in FileStorage.all(FileStorage).keys():
                objs_str_list.append(str(FileStorage.all(FileStorage)[key]))
            print(objs_str_list)
        elif len(line.split(" ")) < 2:
            #ClassName arg is given
            for key in FileStorage.all(FileStorage).keys():
                if key.split('.')[0] == line.split(' ')[0]:
                    print(str(FileStorage.all(FileStorage)[key]))
                else:
                    print("** class doesn't exist **")

    def do_update(self, line):
        #   TO DO : A string argument with a space must be between double quote
                #   Finish the switch/match case satatement
        """Updates an instance based on the class name and id by 
        adding or updating attribute
        Usage: update <class name> <id> <attribute name> \"<attribute value>\""""
        if len(line.split( )) != 4:
            match len(line.split( )):
                case 0:
                    pass
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
            if len(line.split( )) > 4:
                print("Usage: update <class name> <id> "
                      "<attribute name> \"<attribute value>\"")
        else:
            try:
                class_name = line.split(" ")[0]
                id = line.split(" ")[1]
                attrib_name = line.split(" ")[2]
                attrib_value = line.split(" ")[3]
                obj = FileStorage.all(FileStorage)[class_name + "." + id]
                obj.__dict__[attrib_name] = attrib_value
                print("@"*10)
                print(obj.__dict__)
                print("@"*10)
                obj.save()
            except KeyError:
                print("** no instance found **")
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
