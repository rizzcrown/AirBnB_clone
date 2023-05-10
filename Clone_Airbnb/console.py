#!/usr/bin/python3
import cmd
from os import path
import sys
import token
from models.base_models import BaseModel
from models.engine.file_storage import storage
from models.user import User

sys.path.append(path.join(token.__file__, "Clone_Airbnb"))

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) ' # The prompt for user input

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes:
            print("** class doesn't exist **")
        else:
            if arg == 'User':
                new_instance = User()
            else:
                new_instance = storage.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation in an instance"""
        args = arg.split()
        if not args:
            print("** class name missing")
        elif args[0] not in storage.classes:
            print("** class doesn't exist")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            objects = storage.all()
            if obj_key in objects:
                print(objects[obj_key])
            else:
                print("** no instance found **")
    
    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance is missing **")
        else:
            obj_key = args[0] + "." + args[1]
            objects = storage.all()
            if obj_key in objects:
                del objects[obj_key]
                storage.save()
            else:
                print("** no instance found **")
            
    def do_all(self, arg):
        """Prints a string representation of all instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.value()])
        elif arg in storage.classes:
            print([str[obj] for obj in objects.value() if type(obj) == storage.classes[arg]])
        else:
            print("** class doesn't exist **")
    
    def do_update(self, arg):
        """Update an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = args[0] + "." + args[1]
            objects = storage.all()
            if obj_key in objects:
                obj = objects[obj_key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")
    

    def do_quit(self, arg):
        """ Quit the program """
        print("Quiting ...")
        return True
    
    def do_EOF(self, arg):
        """Exit the program on EOF (CtrL+D)"""
        print() # Print newline before exiting 
        return True
    
    def emptyline(self):
        """ Do nothing on an empty line"""
        pass

    def help_quit(self):
        """Display help message for quit command"""
        print("Quit the program")

    def help_EOF(self):
        """ Dispay message of EOF commad"""
        print("Exit the program on EOF (Ctrl+D)")

    def help_help(self):
        """Display help message for help command"""
        print("Show help information for commands")

    def help_emptyline(self):
        """Display help message for empty line"""
        print("Do nothing on an empty line")

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

