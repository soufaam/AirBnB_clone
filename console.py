#!/usr/bin/python3
"""This is  the Entry Point"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


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

    def do_create(self, line):
        """create: Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id. Ex: $ create BaseModel"""

        if not line:
            print("** class name missing **")
        if line != BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            basemodel = BaseModel()
            basemodel.save()
            print(basemodel.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id. Ex: $ sho"""

        commands = line.split()
        if commands == []:
            print("** class name missing **")
            return
        elif commands[0] != BaseModel.__name__:
            print("** class doesn't exist **")
            return
        if len(commands) != 2:
            print("** instance id missing **")
            return
        models.storage.reload()
        key = f'{BaseModel.__name__}.{commands[1]}'
        if key not in models.storage.all().keys():
            print(f"** no instance found **")
        else:
            print(f"{models.storage.all()[key]}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
