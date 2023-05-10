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

    def show(self, arg):
        """Print the string representation in an instance"""
        args = arg.split()
        if not args:
            print("** class name missing")
        elif args[0] not in storage.classes:
            print("** class doesn't exist")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            objects = storage.all()
            instance_found = False
            for obj in objects.value():
                if obj.id == instance_id and (type(obj).__name__ == class_name or instance_id == obj.id):
                    print(obj)
                    instance_found= True
                    break
            if not instance_found:
                print("** no instance found **")
    
    def destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance is missing **")
        else:
            class_name = args[0]
            instance_id = arg[1]
            objects = storage.all()

            if class_name == instance_id:
                #  Deleting the instance by id only
                instance_found = False
                for obj in objects.value():
                    if obj.id == instance_id:
                        instance_found = True
                        del objects[obj.__class__.__name__ + "." + obj.id]
                        storage.save()
                if not instance_found:
                    print("** no instance found **")
            else:
                # Delete the instance by class name and id 
                obj_key = class_name + "." + instance_id
                if obj_key in objects:
                    del objects[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")


    def all(self, arg):
        """Prints a string representation of all instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.value()])
        elif arg in storage.classes:
            print([str[obj] for obj in objects.value() if type(obj) == storage.classes[arg]])
        else:
            print("** class doesn't exist **")
    
    def update(self, arg):
        """ Update an instance based on the class name and id 
            <class name>.update(<id>) - Update an instance based on its ID alone.
            <class name>.update(<id>, <attribute name>, <attribute value>) - Update an instance based on its class name and ID.
            <class name>.update(<id>, <dictionary representation>) - Update an instance based on its class 
            name and ID using a dictionary representation.
        """
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
            class_name = args[0]
            instance_id = args[1]
            update_dict = args[2]
            try:
                update_dict = eval(update_dict)
                if type(update_dict) != dict:
                    raise ValueError
            except (SyntaxError, NameError, ValueError):
                print("** invalid dictionary representation **")
                return
            
            objects = storage.all()
            instance_found = False
            for obj in objects.value():
                if obj.id == instance_id and (obj.__class__.__name__ == class_name or instance_id == obj.id):
                    for key , value in update_dict.items():
                        setattr(obj, key, value)
                    obj.save()
                    instance_found = True
                    break
            if not instance_found:
                print("** no instance found **")
    
    def count(self, arg):
        """Prints the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            count = len([obj for obj in storage.all().values() if isinstance(obj, storage.classes[class_name])])
            print(count)

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

