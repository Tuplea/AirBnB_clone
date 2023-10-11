#!/usr/bin/python3
"""Cmd class : the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quits the command prompt"""
        return True
    
    def do_EOF(self, line):
        """Quits the command prompt"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
