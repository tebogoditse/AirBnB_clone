#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter methods"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        return True

    def help_quit(self, arg):
        message = "Quit command to exit the program"
        print(f"{message}")
    
    def do_EOF(self, arg):
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
