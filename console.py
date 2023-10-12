#!/usr/bin/python3
"""This is  the Entry Point"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import cmd


class HBNBCommand(cmd.Cmd):

    """console.py that contains the
    entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        'An empty line + ENTER shouldn’t execute anything'
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
