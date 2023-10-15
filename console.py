#!/usr/bin/python3
"""
This is  the Entry Point module
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models


class HBNBCommand(cmd.Cmd):

    """console.py that contains the
    entry point of the command interpreter
    """
    classes = {'BaseModel': BaseModel, "User": User,
               "State": State, "City": City, "Amenity": Amenity,
               "Place": Place, "Review": Review}
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program\n
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        'An empty line + ENTER shouldn’t execute anything'
        pass

    def do_create(self, line):
        """
        create: Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """

        if not line:
            print("** class name missing **")
        if line not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            basemodel = self.classes[line]()
            basemodel.save()
            print(basemodel.id)

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id
        """

        commands = line.split()
        if commands == []:
            print("** class name missing **")
            return
        elif commands[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(commands) != 2:
            print("** instance id missing **")
            return
        """models.storage.reload()"""
        key = f'{commands[0]}.{commands[1]}'
        if key not in models.storage.all().keys():
            print(f"** no instance found **")
        else:
            print(f"{models.storage.all()[key]}")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file)
        """

        commands = line.split()
        if commands == []:
            print("** class name missing **")
            return
        elif commands[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(commands) != 2:
            print("** instance id missing **")
            return
        models.storage.reload()
        key = f'{commands[0]}.{commands[1]}'
        if key not in models.storage.all().keys():
            print(f"** no instance found **")
        else:
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name. Ex:
        $ all BaseModel or $ all
        """

        commands = line.split()
        lst = []
        if commands == []:
            for value in models.storage.all().values():
                lst.append(value.__str__())
            print(lst)
        elif commands[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(commands) == 1:
            for key, val in models.storage.all().items():
                if commands[0] in key.split('.')[0]:
                    lst.append(val.__str__())
            print(lst)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email
        "aibnb@mail.com".
        """

        commands = line.split()
        if commands == []:
            print("** class name missing **")
            return
        elif commands[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(commands) < 2:
            print("** instance id missing **")
            return
        key = f'{commands[0]}.{commands[1]}'
        if key not in models.storage.all().keys():
            print(f"** no instance found **")
            return
        if len(commands) < 3:
            print("** attribute name missing **")
            return
        if len(commands) < 4:
            print("** value missing **")
            return
        key = f"{commands[0]}.{commands[1]}"
        setattr(models.storage.all()[key],
                commands[2], commands[3])
        models.storage.all()[key].save()

    def onecmd(self, line):
        """ parseline() to create a tuple containing the command,"""

        lst = []
        class_name, command, line1 = cmd.Cmd.parseline(self, line)
        if class_name in self.classes.keys():
            if command == '.all()':
                for key, val in models.storage.all().items():
                    if class_name in key.split('.')[0]:
                        lst.append(val.__str__())
                print(lst)
            elif command == ".count()":
                for key, val in models.storage.all().items():
                    if class_name in key.split('.')[0]:
                        lst.append(val.__str__())
                print(len(lst))
            elif '.show' in command:
                arg_id = command.split('"')
                if len(arg_id) == 3:
                    key = f'{class_name}.{arg_id[1]}'
                    if key not in models.storage.all().keys():
                        print(f"** no instance found **")
                    else:
                        print(f"{models.storage.all()[key]}")
                else:
                    print("** instance id missing **")
            elif '.destroy' in command:
                arg_id = command.split('"')
                if len(arg_id) == 3:
                    key = f'{class_name}.{arg_id[1]}'
                    if key not in models.storage.all().keys():
                        print(f"** no instance found **")
                    else:
                        del models.storage.all()[key]
                        models.storage.save()
                else:
                    print("** instance id missing **")
            return self.emptyline()
        if not line1:
            return self.emptyline()
        if class_name is None:
            return self.default(line1)
        self.lastcmd = line1
        if line == 'EOF':
            self.lastcmd = ''
        if class_name == '':
            return self.default(line1)
        else:
            try:
                func = getattr(self, 'do_' + class_name)
            except AttributeError:
                return self.default(line1)
            return func(command)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
