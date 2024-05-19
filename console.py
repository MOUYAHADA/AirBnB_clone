#!/usr/bin/python3
"""AirBnB The console"""
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

list_classes = [
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Review",
    "Place"]


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit program"""
        return True

    def do_quit(self, arg):
        """Exit program"""
        return True

    def help_quit(self):
        """Exit program"""
        print("Quit command to exit the program.\n")

    def help_help(self):
        """Help command"""
        print("List available commands or \
              provide help for a specific command.")

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create new instance and print id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] in list_classes:
            print(eval(args[0])().id)
            models.storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show instance based on class name and id"""
        args = arg.split()
        objects = models.storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] in list_classes:
            if len(args) == 2:
                inst_id = f"{args[0]}.{args[1]}"
                if inst_id in objects:
                    print(objects[inst_id])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete instance based on class name and id"""
        objects = models.storage.all()
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] in list_classes:
            if len(args) >= 2:
                inst_id = f"{args[0]}.{args[1]}"
                if inst_id in objects:
                    del objects[inst_id]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Show all instances or all instances of a class"""
        args = arg.split()
        objects = models.storage.all()
        if not arg:
            print([str(objects[key]) for key in objects])
        elif args[0] in list_classes:
            print([str(objects[key])
                  for key in objects if key.startswith(args[0])])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update instance by adding/updating attribute"""
        objects = models.storage.all()
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] in list_classes:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                inst_id = f"{args[0]}.{args[1]}"
                if inst_id in objects:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        try:
                            objects[inst_id].__dict__[args[2]] = eval(args[3])
                            models.storage.save()
                        except SyntaxError:
                            objects[inst_id].__dict__[args[2]] = args[3]
                            models.storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def default(self, args):
        """Default method for class commands"""
        words = args.split(".")
        class_name = words[0]
        if class_name in list_classes:
            command = words[1]
            if command in ["all()", "count()"]:
                if command == "all()":
                    self.do_all(class_name)
                elif command == "count()":
                    self.count(class_name)
            else:
                if "show" in command:
                    my_id = command.split("(")[1].strip(")")
                    self.do_show(f"{class_name} {my_id}")
                elif "destroy" in command:
                    my_id = command.split("(")[1].strip(")")
                    self.do_destroy(f"{class_name} {my_id}")
                elif "update" in command:
                    if "{" not in command.split("(")[1]:
                        myd = command.split("(")[1].split(", ")[0].strip(')"')
                        n_at = command.split("(")[1].split(", ")[1].strip(')"')
                        v_at = command.split("(")[1].split(", ")[2].strip(')"')
                        self.do_update(f"{class_name} {myd} {n_at} {v_at}")
                    elif len(command.split("(")[1].split(", {")) == 2:
                        md = command.split("(")[1].split(", {")[0].strip(')"')
                        s = command.split("(")[1].split(", {")[1].strip(")")
                        dic = eval("{" + s)
                        for atr, val in dic.items():
                            self.do_update(f"{class_name} {md} {atr} {val}")

    def count(self, class_name):
        """Count instances of a class"""
        objects = models.storage.all()
        print(sum(1 for key in objects if key.startswith(class_name)))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
